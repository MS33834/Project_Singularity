FROM python:3.11-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    wget \
    curl \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . /app

# 安装 Python 依赖
RUN pip install --no-cache-dir -r 08_Automation/requirements.txt

# 暴露端口（如需在容器内运行 ComfyUI，需额外配置 GPU 与模型）
EXPOSE 8000

CMD ["python", "08_Automation/preflight_check.py"]
