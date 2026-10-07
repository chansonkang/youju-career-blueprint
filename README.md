# 有据 · Target JD Blueprint

**让每一个职业贡献都有依据。**

面向求职、面试与晋升的开源 Skill 和说明网站。先读目标岗位要求或组织标准，再还原真实项目、核对个人贡献与证据，最后生成职业材料。

**重点适配五类岗位：产品、运营／市场、项目管理、设计、研发。** 其他岗位可以根据实际目标要求调整问题，但当前没有覆盖所有行业或普遍提升求职成功率的验证结论。

[在线网站](https://chansonkang.github.io/youju-career-blueprint/) · [查看 Skill 规则](target-jd-blueprint/SKILL.md) · [职业方法参考](target-jd-blueprint/references/role-lenses.md) · [项目模板](website/materials/真实项目.md) · [参与改进](CONTRIBUTING.md)

## 为什么做这个项目

很多职场人有真实经历，却讲不清为什么做、为什么先做、自己贡献了什么、结果如何证明。文案零散、亮点不突出和量化不足，常常源于项目事实与判断没有整理完整。

有据从项目理解开始，帮助你把「目标要求—工作问题—本人判断—实际行动—结果证据」连接起来。缺少事实时会列出最重要的待补项，不用漂亮的句子替代证据。

## 五类岗位，各有重点

| 重点岗位 | 梳理重点 | 可提供的真实材料 |
| --- | --- | --- |
| **产品** | 用户问题、需求取舍、方案判断、优先级与上线验证 | 访谈、需求文档、方案、实验和行为数据 |
| **运营／市场** | 用户分层、内容与渠道策略、活动链路、成本、质量与归因 | 活动记录、渠道报表、触达与转化口径、预算 |
| **项目管理** | 范围、资源、依赖、风险、关键路径与交付质量 | 项目计划、风险日志、里程碑、变更和验收记录 |
| **设计** | 使用场景、研究、设计取舍、可用性与设计系统 | 原型、研究记录、任务测试和设计交付 |
| **研发** | 技术约束、替代方案、可靠性、性能、维护与工程效率 | 代码、测试、监控、故障、压测和架构记录 |

混合岗位按实际职责组合视角；资历、项目类型、目标 JD 或组织标准决定评价重点。设计不能仅靠改版推导转化提升，研发压测不能直接当成生产效果，团队成绩不能自动归为个人独立完成。

## 可以得到什么

- 目标人才画像、能力维度与准确的岗位表达。
- 一页项目地图：背景、目标、职责、取舍、交付、结果与缺口。
- 证据目录、个人贡献边界及最少待补事项。
- 三种简历策略：成果导向、项目卡片、能力矩阵；保留基础信息、个人亮点、工作经验、项目经历、教育背景五段。
- 面试讲述与追问清单，或按组织标准整理的晋升论证。
- 两类优先级：项目内部先做什么，以及职业材料先讲哪个项目。
- 按要求生成实际 PDF 和同内容的可编辑 Markdown。

网站是使用说明、模拟案例和材料下载入口。**项目分析在支持 Skill 的 AI 对话中进行；网页本身没有模型后端，也不在浏览器中解析上传的简历。** 核心分析无需本项目专用 API key，仍依赖你选择的 AI 工具及其文件处理能力。

## 安装 Skill

克隆或下载本仓库，复制完整的 `target-jd-blueprint/`，不要只复制 `SKILL.md`。

Codex 的默认路径：

```text
~/.codex/skills/target-jd-blueprint/SKILL.md
```

如果设置了 `CODEX_HOME`，使用该目录下的 `skills/`。Windows 使用用户目录下的 `.codex/skills/`。Claude Code 可以放在项目的 `.claude/skills/target-jd-blueprint/` 或个人 `~/.claude/skills/target-jd-blueprint/`，执行时适配实际工具。

安装或更新前保留已有同名版本，避免覆盖自己的改动。完成后开启新对话，调用 `$target-jd-blueprint`。

也可以使用网页中的下载包。仓库中的 [打包脚本](scripts/package_skill.py) 会将当前完整 Skill 打成 ZIP，包含字体与参考文件。

## 第一次使用

准备三样材料：**目标 JD 或晋升标准、一个真实项目、现有证据**。可以附文字型 PDF，也可以直接粘贴原稿；记不清的内容写「未知」，不用先润色。

```text
使用 $target-jd-blueprint。
岗位方向：【产品／运营或市场／项目管理／设计／研发】。
资历：【说明】。场景：【求职简历／面试／晋升】。
我附上目标 JD 或晋升标准、一个真实项目与现有证据。
请先分析目标能力，再还原项目、核对个人贡献和结果，推荐合适写法。
先给我项目地图、表达草稿及最重要的待补项。
没有依据的数字或经历请保留为未知。
请输出 PDF，并保留同内容的 Markdown。
```

仅有 JD 时会先整理目标画像与能力要求，不能生成虚构的个人经历。晋升优先组织真实标准与模板，不强套招聘要求。

### 五类岗位调用示例

- **产品**：「围绕这个 JD 梳理我的需求取舍与验证依据，推荐项目表达顺序。」
- **运营／市场**：「检查活动的渠道、预算、归因窗和转化口径，说明我的实际贡献。」
- **项目管理**：「整理范围变更、依赖和风险处理，形成面试讲述与追问清单。」
- **设计**：「结合原型与测试材料，解释设计判断和可用性证据，未知业务效果留待补。」
- **研发**：「核对技术约束、替代方案和压测条件，区分测试结果与生产效果。」

[目标要求模板](website/materials/目标要求.md) · [真实项目模板](website/materials/真实项目.md) · [证据目录模板](website/materials/证据目录.md)

## PDF 输入、输出和普惠体

文字型 PDF 使用当前环境的 PDF 工具实际读取，保留文件与页码。扫描件依赖可用的 OCR，并需核对识别结果；复杂布局要检查阅读顺序，加密文件需要可读版本。只上传 PDF 不会强制输出 PDF，需要导出时明确说明。

简历排版统一使用 **阿里巴巴普惠体 3.0**，涵盖标题、正文、中英文、数字与页码；PDF 实际嵌入字体，Markdown 保留内容供编辑。默认导出脚本使用随包的 Regular 字体。字体缺失或不可读时明确报错，不自动替换。用户后续明确指定其他字体时遵循新要求。

优先使用 AI 工具自带 PDF 环境。独立运行导出脚本时，Python 3 环境需要 ReportLab；读取 PDF 可使用 pypdf 或 pdfplumber。可选依赖可在自己的虚拟环境安装：

```bash
python3 -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell 使用：.venv\Scripts\Activate.ps1
python -m pip install -r requirements-pdf.txt
python target-jd-blueprint/scripts/export_pdf.py input.md output.pdf
```

脚本支持简单标题、段落、列表和表格，不负责 OCR，也不复制输入 PDF 的版式。文件存在时默认拒绝覆盖；修改对应文件可使用 `--overwrite`。导出后需重开 PDF 核对文字与字体，并用可用的渲染器（如 Poppler）逐页检查排版；脚本执行成功不等于视觉检查完成。

字体适用独立法律声明，不属于 MIT 授权，详见 [素材与字体说明](THIRD_PARTY_NOTICES.md) 和 [PDF 工作流](target-jd-blueprint/references/pdf-workflow.md)。

## 网站本地预览

网页为 HTML / CSS / JavaScript 静态源码，无 npm 安装或构建步骤。在仓库根目录运行：

```bash
python3 scripts/package_skill.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory website
```

打开 `http://127.0.0.1:4173/`。页面提供场景切换、前后表达对照、模拟数据口径、启动指令复制、模板和 Skill 下载。

### 发布到 GitHub Pages

仓库提供 [网页发布脚本](scripts/publish_pages.py)。推送源码到自己的仓库后，在仓库根目录运行 `python3 scripts/publish_pages.py`。脚本先生成最新 Skill 下载包，再将 `website/` 提交到 `gh-pages` 分支；需要 Git 及对 `origin` 的写入权限。已有发布分支会保留其提交历史。

在公开仓库的 **Settings → Pages → Build and deployment → Source** 选择 **Deploy from a branch**，分支选择 **gh-pages**，目录选择 **/ (root)**。后续网页更新时重新运行脚本。源码全部使用相对路径，支持仓库子路径部署；本方案无需个人令牌具备自定义 Actions 工作流写入权限。

部署后以 Actions 返回的实际地址为准。配置依据：[GitHub Pages 官方文档](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 模拟案例与验证边界

[模拟案例](website/demo/项目表达示例.md) 使用两期各 1,000 名新用户、320／460 名完成者，完成率为 32%／46%，相差 14 个百分点。人数、比例和项目情境均为演示假设；前后队列对比不证明独立因果，不代表行业基准、真实业绩或 Skill 带来的业务提升。[数据依据](website/demo/数据依据.md) 保留定义与限制。

目前做过结构校验、部分合成场景行为检查、文字型 PDF 读取／导出与字体检查。尚未全面验证五类岗位的所有资历与行业、扫描件 OCR、复杂版式或实际录用与晋升结果。

## 目录

```text
.
├── target-jd-blueprint/       # 可独立安装的 Skill、职业参考、PDF 脚本与字体
├── website/                  # 静态网页、模板、模拟输入与输出
├── scripts/                  # Skill 打包与 gh-pages 分支发布
├── docs/                     # 材料准备与后续推进模板
├── requirements-pdf.txt      # 独立 PDF 流程的可选依赖
├── CONTRIBUTING.md
├── THIRD_PARTY_NOTICES.md
└── LICENSE
```

## 贡献与来源

欢迎通过 Issue 或 PR 反馈五类重点岗位的真实使用问题，优先提供脱敏或合成的复现材料。公共仓库不包含真实用户简历、联系方式、私有部署身份或账号凭据。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

本 Skill 基于 [uimarch123-arch/target-jd-blueprint](https://github.com/uimarch123-arch/target-jd-blueprint)，基线 commit 为 `a79ac1372fa36cb749208502dcf3474079293c2e`。保留原作者版权及 [MIT 许可](LICENSE)。JD 分析、三套模板与五段结构继承自上游；证据边界、职业视角、晋升适配、PDF 流程、字体约定及网站为本衍生版扩展。[来源记录](target-jd-blueprint/SOURCE.md) 说明继承范围。

代码与文档按 MIT 提供，字体和品牌／装饰图片按独立说明使用；不要把代码许可解释为对所有素材的授权。
