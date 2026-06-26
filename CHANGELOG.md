# 更新日志

> 本文件记录 Project Singularity 的主要变更。格式参考 [Keep a Changelog](https://keepachangelog.com/)。

---

## [Unreleased]

### Added
- 新增 `AIGC_Experience_Chain.md`，说明完整 AIGC 视频生产链路。
- 新增 `CONTRIBUTING.md`、`LICENSE`、`CHANGELOG.md`、`CODE_OF_CONDUCT.md`、`ROADMAP.md`。
- 新增 `examples/` 目录，提供角色提示词、分镜示例、ComfyUI API 载荷示例。
- 新增 `COST_ANALYSIS.md`，包含本地 GPU 与云端 API 成本估算。
- 新增 `TROUBLESHOOTING.md`，汇总常见问题与解决方案。
- 新增 `Dockerfile` 与 `docker-compose.yml`，支持 Docker 快速体验。
- 新增 `Makefile`，提供 `make check/setup/docker/test/sync/clean` 等常用命令。
- 新增 `.github/ISSUE_TEMPLATE/` 与 `.github/PULL_REQUEST_TEMPLATE.md`。
- 新增 `08_Automation/project_health_check.py`，一键检查项目结构完整性。
- 新增 `examples/奇点回响/` 完整案例研究，含制作计划书、制作日志、角色圣经、镜头进度表。
- 新增 `docs/` GitHub Pages 介绍站点，支持中英文切换，与项目视觉风格一致。
- README 新增徽章、Mermaid 架构图、`Makefile` 使用说明与 GitHub Pages 入口。
- README 重写，减少 AI 生成感，强调项目作为开源流程模板的定位。

### Fixed
- 修复 docker-compose.yml 挂载被 .gitignore 忽略的 .env 文件导致新克隆 `make docker` 失败的问题。
- 修复 preflight_check.py 中必需 API 密钥缺失只告警不报错的逻辑 bug。
- 修复 CI 从不运行 pytest 的问题，新增 `pytest` 步骤并使用 `requirements-dev.txt`。
- 修复 Makefile `test` 目标不运行 pytest 且用 `|| true` 吞掉所有预检失败的问题。
- 修复 pyproject.toml 中 `packages.find` 指向无 `__init__.py` 目录的配置错误。
- 修复 `.gitignore` 缺少 `.pytest_cache/` 规则。
- 修复 `.env.example` 中 GITHUB_TOKEN/GITCODE_TOKEN 误导说明（sync_repos.sh 不读取环境变量）。
- 修复 preflight_check.py 检查编号 `[1/8]`…`[8/8]` 与实际 9 步不符的问题。
- 统一两份 `env.example` 内容，补充 `COMFYUI_DIR` 变量文档化。
- 移除 requirements.txt 中未使用的 `python-dotenv`，新增 `requirements-dev.txt` 声明 black/isort/pytest。
- 修正 Ava 资产 README 与生成日志，从虚假的"已生成"改为"待生成"状态。
- 扩展 lint/format 范围覆盖 `tests/` 目录。
- 扩展测试覆盖：新增 docs 站点、案例研究、开发依赖检查。
- 统一 README.md / README.en.md 目录树与实际仓库结构一致。

### Changed
- `07_Team/第二阶段任务分派与执行计划.md`：细化第二阶段任务分工。
- `07_Team/daily_briefs/2026-06-25.md`：更新项目真实状态与下一步计划。

## [0.1.0] - 2025-XX-XX

### Added
- 初始版本：包含项目计划书、任务拆解、四阶段 SOP。
- 24 镜头完整分镜表与 29 张关键帧提示词。
- Flux 角色一致性与 Wan2.2 双专家 ComfyUI 工作流 JSON。
- 16 个自动化脚本，覆盖部署、生成、质检、同步。
- 专家团队分工、任务分派、日报模板、发布模板。
