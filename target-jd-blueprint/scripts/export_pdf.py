#!/usr/bin/env python3
"""Export career Markdown to PDF using embedded Alibaba PuHuiTi 3.0 by default."""
import argparse
import re
from pathlib import Path
from xml.sax.saxutils import escape


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--font', type=Path, help='PuHuiTi font path, or another font explicitly requested by the user.')
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error('Input and output must be different files.')
    if args.output.suffix.lower() != '.pdf':
        parser.error('Output must end in .pdf.')
    if args.output.exists() and not args.overwrite:
        parser.error('Output exists. Use --overwrite only for an authorized revision.')
    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_LEFT
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, LongTable, TableStyle
    except ImportError:
        parser.error('reportlab is required. Use the available bundled PDF runtime.')
    font = args.font or Path(__file__).resolve().parents[1] / 'assets/fonts/AlibabaPuHuiTi-3-55-Regular.ttf'
    if not font.is_file():
        parser.error('PuHuiTi font file is missing. Restore assets/fonts or provide a valid --font path; no fallback font was used.')
    try:
        embedded_font = TTFont('CareerCJK', str(font), subfontIndex=0)
    except Exception as exc:
        parser.error(f'Font could not be loaded: {exc}. No fallback font was used.')
    if args.font is None and b'Alibaba PuHuiTi 3.0' not in embedded_font.face.familyName:
        parser.error('The bundled default font must be Alibaba PuHuiTi 3.0.')
    pdfmetrics.registerFont(embedded_font)
    pdfmetrics.registerFontFamily('CareerCJK', normal='CareerCJK', bold='CareerCJK', italic='CareerCJK', boldItalic='CareerCJK')
    ink, forest = colors.HexColor('#243530'), colors.HexColor('#315548')
    body = ParagraphStyle('Body', fontName='CareerCJK', fontSize=10.5, leading=17,
                          wordWrap='CJK', textColor=ink, spaceAfter=8, alignment=TA_LEFT)
    headings = {
        1: ParagraphStyle('Title', parent=body, fontSize=22, leading=31, spaceAfter=18, keepWithNext=True),
        2: ParagraphStyle('Section', parent=body, fontSize=14, leading=21, textColor=forest, spaceBefore=14, spaceAfter=8, keepWithNext=True),
        3: ParagraphStyle('Sub', parent=body, fontSize=11.5, leading=18, spaceBefore=9, keepWithNext=True),
    }
    cell = ParagraphStyle('Cell', parent=body, fontSize=9, leading=14, spaceAfter=0)
    header = ParagraphStyle('TableHeader', parent=cell, textColor=colors.white)
    text = args.input.read_text(encoding='utf-8')
    if not text.strip():
        parser.error('Input Markdown is empty.')
    missing = sorted({ch for ch in text if not ch.isspace() and not embedded_font.face.charToGlyph.get(ord(ch))})
    if missing:
        parser.error('Font lacks required glyphs: ' + ''.join(missing[:12]) + '. Provide a suitable font from the same family.')
    lines, story, i = text.splitlines(), [], 0
    title = next((l[2:] for l in lines if l.startswith('# ')), args.input.stem)
    def rich(s):
        # Escape user text before allowing only a limited bold markup.
        return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', escape(s.replace('`', '')))
    def table_row(s):
        return [v.strip() for v in s.strip().strip('|').split('|')]
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('|') and i + 1 < len(lines) and re.fullmatch(r'[\s|:\-]+', lines[i + 1]):
            rows = [table_row(line)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(table_row(lines[i]))
                i += 1
            columns = len(rows[0])
            if any(len(row) != columns for row in rows):
                parser.error('Markdown table has inconsistent column counts.')
            data = [[Paragraph(rich(v), header if ri == 0 else cell) for v in row] for ri, row in enumerate(rows)]
            table = LongTable(data, colWidths=[(A4[0] - 96) / columns] * columns, repeatRows=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), forest),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f2f5f2')),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                ('LINEBELOW', (0, 0), (-1, -1), 0.4, colors.HexColor('#d8e1db')),
            ]))
            story.extend([table, Spacer(1, 10)])
            continue
        heading = re.match(r'^(#{1,6})\s+(.+)', line)
        if heading:
            story.append(Paragraph(rich(heading.group(2)), headings[min(len(heading.group(1)), 3)]))
        else:
            if line.startswith(('- ', '* ')):
                line = '- ' + line[2:]
            if line.startswith('> '):
                line = line[2:]
            story.append(Paragraph(rich(line), body))
        i += 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(args.output), pagesize=A4, leftMargin=48, rightMargin=48,
                           topMargin=44, bottomMargin=44, title=title, author='')
    def footer(canvas, document):
        canvas.saveState()
        canvas.setFont('CareerCJK', 8)
        canvas.setFillColor(colors.HexColor('#7e8c84'))
        canvas.drawRightString(A4[0] - 48, 24, str(document.page))
        canvas.restoreState()
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(args.output.resolve())


if __name__ == '__main__':
    main()
