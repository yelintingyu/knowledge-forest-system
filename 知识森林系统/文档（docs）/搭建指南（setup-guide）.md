# 搭建指南：Obsidian + 外部 Work Buddy

## 1. Obsidian 设置
- 安装插件：**Dataview**、**Templater**、**Obsidian Local REST API**（可选，用于外部访问）。
- 在 Templater 设置中，将模板文件夹指定为本项目的 `模板（templates）/`。
- 创建文件夹：`土壤（soil）`, `Trees`, `花朵（Flowers）`, `果实（Fruits）`, `堆肥（Compost）`, `档案（Archive）`。

## 2. Work Buddy 配置（外部 AI 应用）
Work Buddy 是你自行托管的 AI 应用，需具备：
- 读取 Obsidian Vault 的 Markdown 文件。
- 解析 Frontmatter、双链和标签。
- 可在指定位置创建新笔记。
- 所有操作写入 `系统（System）/operation-log.md`（可选但推荐）。

### 推荐实现：Python 脚本 + Local REST API
1. 在 Obsidian 启用 Local REST API 插件（端口 27123）。
2. 部署 `工具（tools）/伙伴示例（obsidian-buddy-example）.py`，它提供：
   - `search`：搜索笔记
   - `read`：读取笔记
   - `create`：创建笔记
   - `bloom`：组合以上功能，调用 AI 开花
3. 通过终端、快捷指令或 iOS 捷径触发脚本。

## 3. 日常操作流程
- **蓄土**：一切碎片丢进 `土壤（soil）`。
- **播种**：用 `种子模板（t-core-seed）` 创建领域种子（如“读书”），可同时多条。
- **生根**：新碎片手动或 AI 打标签并链接；AI 自动扫描新碎片与已有大树的匹配。
- **长干**：用 `几何主干模板（t-geometric-trunk）` 和 `提示词（prompts）/生成主干（generate-trunk）.md` 构建树干。
- **展叶**：用 `叶片模板（t-leaf）` 记录日常知识。
- **开花**：用 `问题模板（t-question）` 写下问题，运行 Work Buddy 命令开多花。
- **结果评级**：
  - 小果直接手动评好/坏。
  - 大果由 Work Buddy 生成 4 个判定标准，确认后执行，执行后 AI 建议评级你确认。
- **修剪**：月底查看黄叶清单，处理长期无链接的土壤碎片。

## 4. 提示词库
将 `提示词（prompts）/` 目录下的提示词导入 Work Buddy，作为技能指令。