# Project Singularity — AIGC 全流程经验链展示

> 本文件面向面试官、合作伙伴、技术社区读者，以及希望把本仓库作为 **AIGC 作品集** 的开发者。
>
> 核心信息：
> - 本仓库不是一部已完成的影片，而是一条**可复用的 AIGC 工业化生产流程链**。
> - 它以科幻微短剧《奇点回响》为示例载体，覆盖从剧本到 4K 母版的完整链路。
> - 所有剧本、角色、镜头、提示词均可替换，流程本身才是重点。

---

## 一、这条经验链能证明什么能力？

| 能力维度 | 本仓库对应内容 | 可回答的问题 |
|----------|----------------|--------------|
| **AIGC 项目策划** | 项目计划书、任务拆解、进度检查清单 | 你如何把 AIGC 创意变成可执行项目？ |
| **大模型文本生成** | 剧本、世界观、角色圣经 | 你如何用 DeepSeek/Claude 做创意策划？ |
| **AI 图像生成与角色一致性** | Flux.1 Kontext + IPAdapter 工作流、角色参考图规范 | 你如何解决 AI 视频中「同一个人变来变去」的问题？ |
| **AI 视频生成** | Wan2.2 I2V 14B 双专家工作流、可灵 2.5 Turbo API | 你如何生成稳定、不闪烁、符合物理逻辑的镜头？ |
| **后期与音效** | 达芬奇调色、Topaz 超分、ElevenLabs 配音、Suno 配乐 SOP | 你如何做 AI 视频的后期合成与音频设计？ |
| **工程化与自动化** | 16 个 Python/Shell 脚本、ComfyUI API、渲染队列 | 你如何用代码把 AIGC 流程工业化？ |
| **项目管理与质量管控** | 专家团队、任务分派、QA 检测、盲测方案、风险清单 | 你如何保证 AIGC 项目可控、可验收？ |
| **社区与发布** | 发布检查清单、教程模板、答辩 PPT 模板 | 你如何把 AIGC 成果对外发布与传播？ |

---

## 二、经验链全流程图

```
策划层
├── 项目计划书、任务拆解、预算与风险管理
├── 剧本与世界观（DeepSeek / Claude）
└── 角色圣经与分镜表
      ↓
资产层
├── Flux.1 Kontext + IPAdapter 角色一致性出图
├── 艾娃多角度参考图（正/侧/背/表情）
└── 29 张场景关键帧（24 镜头 + 5 组首尾帧）
      ↓
动态层
├── Wan2.2 I2V 14B High/Low Noise 双专家 → 19 个标准镜头
└── 可灵 2.5 Turbo 首尾帧约束 → 5 个复杂/转场镜头
      ↓
合成层
├── 剪映/达芬奇粗剪与锁定剪辑
├── ElevenLabs 角色配音
├── Suno/Udio 科幻配乐
├── 环境音效与 Foley
├── Topaz Video AI 4K 超分与降噪
└── 达芬奇 Teal & Orange 调色
      ↓
发布层
├── 4K 母版输出
├── ComfyUI 工作流 JSON 打包
├── SOP 手册归档
└── 全平台发布 + 技术社区教程
```

---

## 三、各阶段能力证明点

### 3.1 第一阶段：资产铸造与技术验证

**核心目标**：证明你能在 AI 生成中做到「角色一致性」。

| 能力 | 证明方式 | 对应文件 |
|------|----------|----------|
| 剧本创作 | 完整科幻剧本与分镜 | [`02_Scripts/奇点回响_剧本与世界观.md`](./02_Scripts/奇点回响_剧本与世界观.md) |
| 角色设计 | 角色圣经 + 视觉锚点 | [`02_Scripts/角色圣经_模板.md`](./02_Scripts/角色圣经_模板.md) |
| 提示词工程 | 24 镜头关键帧提示词 | [`02_Scripts/关键帧提示词汇总表.md`](./02_Scripts/关键帧提示词汇总表.md) |
| 角色一致性 | Flux.1 Kontext + IPAdapter 工作流 | [`03_Workflows/Flux_Character_Consistency.json`](./03_Workflows/Flux_Character_Consistency.json) |
| 质量验证 | 盲测方案与 QA 检查表 | [`06_Research/QA测试与盲测方案.md`](./06_Research/QA测试与盲测方案.md) |

**可讲的故事**：
> "在 AIGC 视频里，角色『变脸』是最常见的问题。我通过角色圣经固定服装锚点，用 IPAdapter 绑定多角度参考图，再用盲测验证跨镜头一致性，把这个问题工程化了。"

---

### 3.2 第二阶段：动态镜头生产

**核心目标**：证明你能用 AI 稳定生成符合叙事意图的视频。

| 能力 | 证明方式 | 对应文件 |
|------|----------|----------|
| 本地视频生成 | Wan2.2 I2V 14B 双专家工作流 | [`03_Workflows/Wan22_Dual_Expert_Video.json`](./03_Workflows/Wan22_Dual_Expert_Video.json) |
| 复杂镜头控制 | 可灵 2.5 Turbo 首尾帧 API | [`08_Automation/kling_video_api.py`](./08_Automation/kling_video_api.py) |
| 自动化批处理 | 关键帧批量生成、分镜转视频脚本 | [`08_Automation/batch_keyframe_gen.py`](./08_Automation/batch_keyframe_gen.py)、[`storyboard_to_video.py`](./08_Automation/storyboard_to_video.py) |
| 参数调优 | CFG/Denoise 调优记录 | [`06_Research/参数调优记录表.md`](./06_Research/参数调优记录表.md) |
| 质量检测 | 视频闪烁/崩坏自动检测 | [`08_Automation/video_quality_check.py`](./08_Automation/video_quality_check.py) |

**可讲的故事**：
> "标准镜头用本地 Wan2.2 跑，复杂转场镜头用可灵首尾帧约束；High Noise 专家负责运动幅度，Low Noise 专家负责修复崩坏帧，这是典型的云端-本地混合 AIGC 管线。"

---

### 3.3 第三阶段：后期合成与音效设计

**核心目标**：证明你能把 AI 素材变成「电影感」成片。

| 能力 | 证明方式 | 对应文件 |
|------|----------|----------|
| 剪辑叙事 | 粗剪/锁定剪辑模板 | [`05_Output/Rough_Cuts/`](./05_Output/Rough_Cuts/) |
| AI 配音 | ElevenLabs API 调用 | [`08_Automation/elevenlabs_tts_api.py`](./08_Automation/elevenlabs_tts_api.py) |
| AI 配乐 | Suno API 调用 | [`08_Automation/suno_music_api.py`](./08_Automation/suno_music_api.py) |
| 音效设计 | 环境音/Foley 规范 | [`04_SOP/音频制作规范.md`](./04_SOP/音频制作规范.md) |
| 画质增强 | Topaz Video AI 超分规范 | [`05_Output/Final/upscale_and_repair_notes.md`](./05_Output/Final/upscale_and_repair_notes.md) |
| 调色 | 达芬奇 Teal & Orange 电影感调色 | [`05_Output/Final/color_grading_notes.md`](./05_Output/Final/color_grading_notes.md) |

**可讲的故事**：
> "AI 生成只是素材，真正做成片还需要剪辑节奏、配音情绪、配乐氛围、Topaz 超分和达芬奇调色。我把每个环节都写成了 SOP，保证可复现。"

---

### 3.4 第四阶段：成片发布与工作流封装

**核心目标**：证明你能把个人能力沉淀为团队/社区可复用的资产。

| 能力 | 证明方式 | 对应文件 |
|------|----------|----------|
| 工作流封装 | ComfyUI JSON 打包脚本 | [`08_Automation/package_workflows.sh`](./08_Automation/package_workflows.sh) |
| 文档沉淀 | SOP 手册、后期规范、音频规范 | [`04_SOP/SOP_Project_Singularity.md`](./04_SOP/SOP_Project_Singularity.md) |
| 发布运营 | 全平台发布检查清单 | [`09_Release/release_checklist.md`](./09_Release/release_checklist.md) |
| 社区传播 | 技术教程模板 | [`09_Release/tutorial_template.md`](./09_Release/tutorial_template.md) |
| 项目答辩 | 展示 PPT 模板 | [`09_Release/presentation_template.md`](./09_Release/presentation_template.md) |

---

## 四、工程化与协作能力

除了创意和生成，本仓库还展示了**把 AIGC 流程工程化**的能力：

| 工程能力 | 对应文件 |
|----------|----------|
| 环境自动化部署 | [`08_Automation/deploy_comfyui.sh`](./08_Automation/deploy_comfyui.sh) |
| 环境预检 | [`08_Automation/preflight_check.py`](./08_Automation/preflight_check.py) |
| 性能基准测试 | [`08_Automation/benchmark.py`](./08_Automation/benchmark.py) |
| 渲染队列管理 | [`08_Automation/render_queue.py`](./08_Automation/render_queue.py) |
| 资产进度看板 | [`08_Automation/asset_dashboard.py`](./08_Automation/asset_dashboard.py) |
| 每日简报生成 | [`08_Automation/daily_brief.py`](./08_Automation/daily_brief.py) |
| 双仓库同步 | [`08_Automation/sync_repos.sh`](./08_Automation/sync_repos.sh) |
| 项目进度管理 | [`项目进度检查清单.md`](./项目进度检查清单.md)、[`tasks.md`](./tasks.md) |
| 风险与合规 | [`06_Research/授权合规清单.md`](./06_Research/授权合规清单.md)、[`06_Research/数据备份与版本控制方案.md`](./06_Research/数据备份与版本控制方案.md) |

---

## 五、如何用这个仓库讲 AIGC 经验？

### 5.1 给面试官看（5 分钟版本）

1. 打开 README 和本文件，说明这是一个 **AIGC 工业化流程模板**。
2. 展示 [`项目计划书_完整版.md`](./项目计划书_完整版.md) 中的「源-流-汇」架构图。
3. 展示 [`03_Workflows/`](./03_Workflows/) 中的 Flux 和 Wan2.2 工作流 JSON。
4. 展示 [`08_Automation/`](./08_Automation/) 中的自动化脚本，强调工程化能力。
5. 展示 [`04_SOP/SOP_Project_Singularity.md`](./04_SOP/SOP_Project_Singularity.md) 中的全流程规范。

### 5.2 给技术社区看（博客/教程版本）

1. 用 [`09_Release/tutorial_template.md`](./09_Release/tutorial_template.md) 改成一篇实战教程。
2. 重点写「角色一致性」和「Wan2.2 双专家」两个技术亮点。
3. 附上 ComfyUI 工作流 JSON 和关键参数截图。
4. 把链接发布到知乎/公众号/B 站专栏/GitHub Discussions。

### 5.3 给团队/教师看（答辩版本）

1. 用 [`09_Release/presentation_template.md`](./09_Release/presentation_template.md) 制作 PPT。
2. 强调**流程可复制、团队可协作、质量可验收**。
3. 展示 [`07_Team/expert_team.md`](./07_Team/expert_team.md) 和 [`07_Team/第二阶段任务分派与执行计划.md`](./07_Team/第二阶段任务分派与执行计划.md)。

---

## 六、当前仓库状态（真实 vs 占位）

| 类型 | 状态 | 说明 |
|------|------|------|
| 计划/文档/SOP | ✅ 完整 | 可直接作为经验链展示 |
| ComfyUI 工作流 JSON | ✅ 完整 | 包含 Flux 和 Wan2.2 两个核心工作流 |
| 自动化脚本 | ✅ 完整 | 16 个脚本覆盖部署、生成、质检、同步 |
| 剧本/分镜/提示词 | ✅ 完整 | 24 镜头完整分镜与 29 张关键帧提示词 |
| 角色参考图 PNG | ⏳ 占位 | 已写生成脚本与日志，可在 RTX 4090 环境生成 |
| 关键帧 PNG | ⏳ 占位 | 同上 |
| 视频 MP4 | ⏳ 占位 | 同上 |
| 音频素材 | ⏳ 占位 | 同上 |
| 最终成片 | ⏳ 占位 | 同上 |

> 对于作品集用途，**流程、代码、文档、SOP 的完整性已经足够证明 AIGC 经验**。实际 PNG/MP4 可在有 GPU 的环境一键生成，不影响经验链的展示价值。

---

## 七、推荐阅读路径

如果你是第一次看这个仓库，建议按以下顺序阅读：

1. [`README.md`](./README.md) — 项目总览
2. [`项目计划书_完整版.md`](./项目计划书_完整版.md) — 完整规划与技术架构
3. [`AIGC_Experience_Chain.md`](./AIGC_Experience_Chain.md) — 本文件，经验链展示
4. [`04_SOP/SOP_Project_Singularity.md`](./04_SOP/SOP_Project_Singularity.md) — 全流程操作手册
5. [`08_Automation/README.md`](./08_Automation/README.md) — 自动化脚本说明
6. [`07_Team/expert_team.md`](./07_Team/expert_team.md) — 团队与角色分工
7. [`09_Release/presentation_template.md`](./09_Release/presentation_template.md) — 答辩/展示模板

---

> 本文件由项目团队维护，随经验链完善持续更新。
