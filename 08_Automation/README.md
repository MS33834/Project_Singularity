# Project Singularity — 自动化脚本说明

本目录存放项目中各 AI 服务的 API 调用脚本，用于批量生成复杂镜头视频、配音与配乐。

## 文件清单

| 文件 | 用途 |
|------|------|
| `kling_video_api.py` | 可灵 2.5 Turbo 图生视频（含首尾帧） |
| `elevenlabs_tts_api.py` | ElevenLabs 文本转语音，生成艾娃与核心对白 |
| `suno_music_api.py` | Suno AI 科幻氛围配乐生成 |
| `requirements.txt` | Python 依赖 |

## 快速开始

1. 安装依赖：

```bash
pip install -r requirements.txt
```

2. 配置环境变量（推荐）或修改脚本中的配置区：

```bash
export KLING_API_KEY="your_kling_api_key"
export ELEVENLABS_API_KEY="your_elevenlabs_api_key"
export SUNO_API_KEY="your_suno_api_key"
```

3. 运行脚本：

```bash
python kling_video_api.py
python elevenlabs_tts_api.py
python suno_music_api.py
```

## 重要提示

- 可灵官方 API 与第三方聚合平台（PiAPI、Runware、CometAPI）的 endpoint、参数、鉴权方式不同，使用前请确认文档。
- Suno 官方 API 目前为邀请制，若无法获取 API，可直接使用网页版生成后下载。
- ElevenLabs 的 `voice_id` 请在控制台中查看并替换为实际值。
- 所有脚本默认输出路径为 `../01_Assets/` 或 `../05_Output/`，请确保从 `08_Automation/` 目录运行。

## 输出规范

- 视频：`../05_Output/Rough_Cuts/场景号_工具_版本.mp4`
- 配音：`../01_Assets/Audio/Voices/角色_序号.wav`
- 配乐：`../01_Assets/Audio/Music/曲名_v1.mp3`
