# Project Singularity — ComfyUI 工作流说明

本目录存放《奇点回响》项目调试完成的 ComfyUI 工作流 JSON 文件。

## 文件清单

| 文件 | 用途 | 状态 |
|------|------|------|
| `Flux_Character_Consistency.json` | Flux.1 Kontext + IPAdapter 角色一致性出图 | 待 ComfyUI 中搭建后替换为实际 JSON |
| `Wan22_Dual_Expert_Video.json` | Wan2.2 I2V 14B High/Low Noise 双专家视频生成 | 待 ComfyUI 中搭建后替换为实际 JSON |

## 如何生成最终工作流 JSON

1. 在 ComfyUI 中按 `04_SOP/SOP_Project_Singularity.md` 搭建节点。
2. 点击 ComfyUI 右上角 **Save** 按钮，保存为 JSON。
3. 将保存的 JSON 覆盖本目录下的同名文件。
4. 在 `节点依赖.md` 中记录所用自定义节点与版本。

## 推荐节点依赖

### Flux_Character_Consistency

- `ComfyUI` 最新版
- `ComfyUI-Manager`
- `ComfyUI-IPAdapter-Plus`
- `ComfyUI_PuLID_Flux`（可选）
- `FLUX.1-Kontext-dev` 模型权重

### Wan22_Dual_Expert_Video

- `ComfyUI` 最新版（≥0.3.46）
- `ComfyUI-Manager`
- `ComfyUI-WanVideoWrapper` 或原生 Wan 节点
- `Wan2.2-I2V-A14B` FP8 量化模型
- `Wan2.2 VAE`
- `umt5_xxl_fp8_e4m3fn_scaled` 文本编码器

## 参数预设

详见各 JSON 文件中的 `_meta.parameters` 字段。
