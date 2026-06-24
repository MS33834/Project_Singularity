# Project Singularity — 自动化脚本说明

本目录存放项目中所有自动化脚本，涵盖环境部署、批量生成、API 调用、质量检测与项目管理。

> 所有脚本均使用 `PROJECT_ROOT = Path(__file__).resolve().parent.parent` 定位项目根目录，可从任意目录运行。

## 文件清单

### 环境与部署

| 文件 | 用途 |
|------|------|
| `deploy_comfyui.sh` | 部署 ComfyUI 环境与必要节点 |
| `init_git.sh` | 初始化 Git 仓库与 .gitignore |
| `preflight_check.py` | 预飞行环境检查（GPU/内存/磁盘/模型/API 密钥） |
| `benchmark.py` | ComfyUI 性能基准测试（Flux/Wan2.2/可灵） |
| `requirements.txt` | Python 依赖清单 |

### 批量生成

| 文件 | 用途 |
|------|------|
| `batch_keyframe_gen.py` | 通过 ComfyUI API 批量生成关键帧 |
| `storyboard_to_video.py` | 分镜到视频流水线（Wan2.2 I2V/T2V） |
| `kling_video_api.py` | 可灵 2.5 Turbo 图生视频（含首尾帧） |
| `elevenlabs_tts_api.py` | ElevenLabs 文本转语音，生成角色对白 |
| `suno_music_api.py` | Suno AI 科幻氛围配乐生成 |
| `render_queue.py` | 渲染队列管理器（批量任务/优先级/重试） |

### 质量与管理

| 文件 | 用途 |
|------|------|
| `video_quality_check.py` | 视频质量自动检测（分辨率/帧率/闪烁/锐度） |
| `asset_dashboard.py` | 资产盘点与进度看板 |
| `daily_brief.py` | 每日站会简报生成 |

### 仓库同步

| 文件 | 用途 |
|------|------|
| `sync_repos.sh` | GitHub/GitCode 双仓库同步推送 |
| `package_workflows.sh` | ComfyUI 工作流 JSON 打包发布 |

## 快速开始

1. 安装依赖：

```bash
pip install -r requirements.txt
# PyTorch 请按 CUDA 版本单独安装: https://pytorch.org
```

2. 配置环境变量（推荐写入 .env 或直接 export）：

```bash
export KLING_API_KEY="your_kling_api_key"
export ELEVENLABS_API_KEY="your_elevenlabs_api_key"
export SUNO_API_KEY="your_suno_api_key"
export COMFYUI_URL="http://127.0.0.1:8188"
```

3. 预飞行检查：

```bash
python preflight_check.py
```

4. 批量生成：

```bash
python batch_keyframe_gen.py        # 关键帧
python storyboard_to_video.py       # 视频
python kling_video_api.py            # 复杂镜头
python elevenlabs_tts_api.py         # 配音
python suno_music_api.py             # 配乐
```

5. 质量与管理：

```bash
python video_quality_check.py        # 视频质检
python asset_dashboard.py            # 资产看板
python daily_brief.py                # 站会简报
```

## 输出规范

- 关键帧：`01_Assets/Scenes/PS_{镜头号}_v01.png`
- 视频：`05_Output/Rough_Cuts/PS_{镜头号}_{工具}_v01.mp4`
- 配音：`01_Assets/Audio/Dialogue/{角色}_{序号}.wav`
- 配乐：`01_Assets/Audio/Music/{曲名}_v1.mp3`
- 日志：`06_Research/video_gen_log.csv`
- 报告：`06_Research/*.md`
