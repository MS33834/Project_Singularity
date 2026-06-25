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
- README 新增徽章、Mermaid 架构图、`Makefile` 使用说明。
- README 重写，减少 AI 生成感，强调项目作为开源流程模板的定位。

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
