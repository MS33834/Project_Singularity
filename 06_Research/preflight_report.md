# 预飞行检查报告

**时间**: 2026-06-25 09:29:44

**结果**: 失败

| 类别 | 数量 |
|------|------|
| 通过 | 16 |
| 警告 | 6 |
| 错误 | 5 |

## 致命错误

- PyTorch 未安装
- Python 包未安装: torch（pip install torch）
- Python 包未安装: requests（pip install requests）
- Python 包未安装: Pillow（pip install Pillow）
- ComfyUI 目录不存在: /root/ComfyUI

## 警告

- 内存 3.8GB 低于推荐 32GB
- 可用空间 7.4GB 低于推荐 100GB（视频素材占用大）
- ComfyUI 目录不存在，跳过模型检查
- KLING_API_KEY: 未配置 (可灵视频生成)
- ELEVENLABS_API_KEY: 未配置 (ElevenLabs 配音)
- SUNO_API_KEY: 未配置 (Suno 配乐（可选）)
