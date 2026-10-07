# target-jd-blueprint · 有据改进版

基于 [uimarch123-arch/target-jd-blueprint](https://github.com/uimarch123-arch/target-jd-blueprint) 的 MIT 衍生版。保留原名称与 JD→画像→能力/话术→三模板→素材→Markdown 成果流程；基线为 `a79ac1372fa36cb749208502dcf3474079293c2e`，原作者版权及许可见 [LICENSE](LICENSE)。

本版先用真实项目和证据支持经历，再按目标要求组织表达。JD 是要求与措辞来源，不能证明用户做过某项工作。新增项目地图、贡献边界、证据编号、两类优先级和晋升场景；不再强制每一步确认或依赖 Claude 特定工具名。

## 安装本次改进版

下载网页中的 `target-jd-blueprint.zip` 并解压，或从仓库中复制完整的 `target-jd-blueprint/`。将其中完整的 `target-jd-blueprint` 文件夹放到 Codex 的 `$CODEX_HOME/skills/`；没有配置时为 `~/.codex/skills/target-jd-blueprint/`。最终入口文件应是 `~/.codex/skills/target-jd-blueprint/SKILL.md`，不要多套一层同名目录。

若已有同名 Skill，先保留原目录并核对版本，再决定迁移。克隆上游仓库得到的是原版；使用此包才能得到本次改进内容。核心分析无需 API key、网站服务或专用运行脚本；附带 PDF 导出脚本需要 Python、ReportLab 与可嵌入中文字体，优先使用 Codex 自带 PDF 环境。

Claude Code 中也可使用 `.claude/skills/target-jd-blueprint/`；执行时适配实际可用的工具。避免同时启用承担相同工作入口的重复 Skill。

## 第一次使用

在新对话中输入：

> 使用 `$target-jd-blueprint`。我是【职业/资历】，准备【求职目标或晋升级别】。这是我的目标 JD 或晋升标准：【原文】；这是一个真实项目：【原始描述】；现有证据：【记录或本人回忆】。请先分析目标、梳理项目，再做【简历/面试/晋升材料】，未知处逐步问我。

一份 JD、一个项目即可起步；缺标准或数据明确写不知道，不用补编资料。也可以填写仓库 `website/materials/` 中的 3 份材料模板。仅有 JD 时先输出人才画像、能力维度与话术，经历等用户提供后再写。

## 三套简历策略与输出

- 成果导向：已有可信结果证据，成果优先。
- 项目卡片：解释代表项目的问题、选择、本人动作与交付；只有一个项目也适用。
- 能力矩阵：将目标要求映射到真实证据，适合转型或复合背景。

简历保留基础信息、个人亮点、工作经验、项目经历、教育背景五段；项目含背景、职责、成果。保存真实 `.md` 文件，并附项目地图、证据与待补事项。面试按实际经历形成讲述和追问；晋升优先组织要求与模板，不套招聘权重。

材料可以是回忆、原稿、代码/设计/测试、验收、复盘或报表。未知业务数字时可写有依据的交付，不能声称不存在的效果。团队结果与本人贡献分别说明。历史 AI PM 基线仅用于相关岗位，原记录的 10 份 JD 样本本次未重新核验。

## 行业与 PDF 文件

本版重点适配产品、运营／市场、项目管理、设计、研发五类岗位；核心流程可按实际标准调整。其他职业依实际 JD 或组织标准适配；尚未验证所有行业，不替代行业资格或组织职级要求。

可在对话附上文字型 PDF 并要求“请输出 PDF，并保留同内容的 Markdown”。先实际提取、核对原文件与页码，再生成新文件。扫描件需具备 OCR 并核对，复杂版式需视觉检查；加密文件需可读版本。PDF 导出并不保留原文件版式。

执行细节见 [PDF 工作流](references/pdf-workflow.md)。其中的 `scripts/export_pdf.py` 支持简单标题、段落、列表、表格。没有工具、中文字体或可读原文时明确说明限制，保留可编辑材料，不声称已导出 PDF。

## 目录

```text
target-jd-blueprint/
├── SKILL.md
├── README.md
├── LICENSE
├── SOURCE.md
├── agents/openai.yaml
├── scripts/export_pdf.py
├── assets/
│   ├── fonts/  # 普惠体 Regular、字体法律声明与来源
│   ├── resume-formula-bank.md
│   └── phrase-bank.md
└── references/
    ├── extraction-and-weighting.md
    ├── default-ai-pm-dimensions.md
    ├── interview.md
    ├── role-lenses.md
    ├── priorities.md
    ├── pdf-workflow.md
    └── evidence-and-writing.md
```

## 当前验证边界

结构校验与合成素材的行为测试不能证明求职/晋升成功或普遍效果。真实试用先从一个项目开始，用户核对关键事实，再补最重要证据；按实际问题迭代。没有真实岗位标准、项目记录或可比结果时，明确保留限制。

## 简历字体约定

简历排版统一使用阿里巴巴普惠体 3.0，覆盖标题、正文、中文、英文、数字及页眉页脚。PDF 实际嵌入字体并核对；Markdown 保留可编辑内容。导出脚本默认使用随包的普惠体 Regular，字体缺失时明确报错，不自动换字体。用户后续明确指定其他字体时遵循新要求。字体的独立法律声明与来源位于 `target-jd-blueprint/assets/fonts/`（Skill 目录内为 `assets/fonts/`）。
