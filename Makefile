.PHONY: help check setup docker test sync clean

help:
	@echo "Project Singularity — 常用命令"
	@echo "  make check     检查项目结构是否完整"
	@echo "  make setup     安装 Python 依赖"
	@echo "  make docker    使用 Docker 启动容器"
	@echo "  make test      运行基础测试"
	@echo "  make sync      同步推送至 GitHub 与 GitCode"
	@echo "  make clean     清理临时文件"

check:
	python 08_Automation/project_health_check.py

setup:
	pip install -r 08_Automation/requirements.txt

docker:
	docker compose up -d

test:
	python 08_Automation/project_health_check.py
	python 08_Automation/preflight_check.py

sync:
	bash 08_Automation/sync_repos.sh

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.log" -delete
