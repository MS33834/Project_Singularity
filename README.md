# Project Singularity | 奇点回响

> AIGC 全流程原创科幻微短剧工业化生产流程验证项目
>
> **本仓库沉淀的是一套可复用的 AIGC 视频工业化流程模板。**  
> Project Singularity /《奇点回响》仅作为示例载体，用于演示各环节如何落地。  
> 剧本、角色、镜头、对白、配乐等所有具体内容，均可按你的实际项目替换。

## 仓库地址

| 平台 | 地址 |
|------|------|
| GitHub | https://github.com/MS33834/Project_Singularity |
| GitCode | https://gitcode.com/badhope/Project_Singularity |

> 每完成一个阶段，使用 `bash 08_Automation/sync_repos.sh "提交信息"` 同步推送至双仓库。

## 项目信息

- **项目代号**：Project Singularity
- **中文名**：奇点回响
- **项目性质**：AIGC 全流程原创微短剧 / 技术验证与工作流沉淀 / 可复用流程模板
- **拟定周期**：6 周
- **目标成片时长**：3-5 分钟
- **目标分辨率**：4K
- **撰写日期**：2025 年

## 目录结构

```
Project_Singularity/
├── 01_Assets/              # 资产库
│   ├── Characters/         # 角色资产（艾娃等）
│   ├── Scenes/             # 场景关键帧与概念图
│   └── Audio/              # 音效、配音、配乐素材
├── 02_Scripts/             # 剧本、世界观、角色圣经、分镜、提示词
├── 03_Workflows/           # ComfyUI JSON 工作流 + 节点依赖
├── 04_SOP/                 # SOP 操作手册 + 后期制作规范 + 音频制作规范
├── 05_Output/              # 输出成片
│   ├── Rough_Cuts/         # 粗剪版本
│   └── Final/              # 最终成片
├── 06_Research/            # 技术栈、预算、授权合规、备份方案、发布计划、调优、失败案例
├── 07_Team/                # 专家名册、任务分派、启动会
├── 08_Automation/          # 部署脚本、API 调用、基准测试
├── 项目计划书_完整版.md     # 教师可跟随审阅的完整计划书
├── 项目进度检查清单.md      # 可勾选/划掉的全流程进度表
├── 教师评审表_模板.md       # 各阶段里程碑验收表
└── 周报模板.md              # 每周师生同步会汇报模板
```

## 核心技术栈

| 层级 | 技术组件 | 用途 |
|------|---------|------|
| 源：一致性与资产层 | DeepSeek / Claude | 剧本与角色圣经生成 |
| | Flux.1 Kontext Dev + PuLID + IPAdapter | 角色一致性出图 |
| 流：动态与叙事层 | Wan2.2 I2V 14B（High/Low Noise 双专家） | 标准镜头视频生成 |
| | 可灵 2.5 Turbo（首尾帧约束） | 高复杂度/转场镜头 |
| 汇：合成与发布层 | 剪映专业版 / 达芬奇 | 剪辑与调色 |
| | Suno / Udio + ElevenLabs | 配乐与配音 |
| | Topaz Video AI / After Effects | 画质增强与修复 |

## 关键验收指标

1. 跨镜头角色相似度 > 95%（团队盲测通过）
2. 输出 40-60 个原始视频片段
3. 最终成片 3-5 分钟，4K 分辨率，含完整音效
4. 沉淀标准化 ComfyUI 工作流 JSON 与 SOP 手册

## 快速开始

1. 查看 [`项目计划书_完整版.md`](./项目计划书_完整版.md) 了解完整项目规划（教师可跟随审阅）
2. 查看 [`项目进度检查清单.md`](./项目进度检查清单.md) 了解可勾选/划掉的全流程进度表
3. 查看 [`tasks.md`](./tasks.md) 了解四阶段任务拆解
4. 查看 [`07_Team/expert_team.md`](./07_Team/expert_team.md) 了解专家团队名册
5. 查看 [`07_Team/任务分派与启动会.md`](./07_Team/任务分派与启动会.md) 了解第一周任务分派
6. 查看 [`02_Scripts/奇点回响_剧本与世界观.md`](./02_Scripts/奇点回响_剧本与世界观.md) 阅读完整剧本
7. 查看 [`02_Scripts/详细分镜表.md`](./02_Scripts/详细分镜表.md) 查看 24 镜头详细分镜
8. 查看 [`02_Scripts/关键帧提示词汇总表.md`](./02_Scripts/关键帧提示词汇总表.md) 获取 24 镜头提示词
9. 查看 [`04_SOP/SOP_Project_Singularity.md`](./04_SOP/SOP_Project_Singularity.md) 查看完整 SOP
10. 查看 [`04_SOP/后期制作规范.md`](./04_SOP/后期制作规范.md) 查看剪辑/调色/超分规范
11. 查看 [`04_SOP/音频制作规范.md`](./04_SOP/音频制作规范.md) 查看配音/配乐/混音规范
12. 查看 [`06_Research/`](./06_Research/) 了解技术栈、预算、授权、备份、发布、调优、失败案例
13. 查看 [`08_Automation/`](./08_Automation/) 获取部署脚本与 API 调用代码

## 开发者快速启动

```bash
# 1. 初始化 Git 仓库
cd /workspace/Project_Singularity
bash 08_Automation/init_git.sh

# 2. 部署 ComfyUI 环境
bash 08_Automation/deploy_comfyui.sh

# 3. 性能基准测试
cd ~/ComfyUI && source venv/bin/activate
python /workspace/Project_Singularity/08_Automation/benchmark.py

# 4. 配置 API 密钥
export KLING_API_KEY="your_key"
export ELEVENLABS_API_KEY="your_key"
export SUNO_API_KEY="your_key"
export COMFYUI_URL="http://127.0.0.1:8188"

# 5. 批量生成关键帧（需先在 ComfyUI 中保存 API 格式 JSON）
cd /workspace/Project_Singularity/08_Automation
pip install -r requirements.txt
python batch_keyframe_gen.py

# 6. 批量生成视频
python storyboard_to_video.py

# 7. 生成复杂镜头（可灵）、配音、配乐
python kling_video_api.py
python elevenlabs_tts_api.py
python suno_music_api.py
```
