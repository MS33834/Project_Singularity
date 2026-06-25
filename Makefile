.PHONY: help check setup docker test lint format sync clean

help:
	@echo "Project Singularity — Common commands"
	@echo "  make check     Verify project structure"
	@echo "  make setup     Install Python dependencies"
	@echo "  make docker    Start Docker container"
	@echo "  make test      Run all checks"
	@echo "  make lint      Run linters (black, isort)"
	@echo "  make format    Auto-format code"
	@echo "  make sync      Push to GitHub and GitCode"
	@echo "  make clean     Remove temp files"

check:
	python 08_Automation/project_health_check.py

setup:
	pip install -r 08_Automation/requirements.txt

docker:
	docker compose up -d

test: check lint
	python 08_Automation/preflight_check.py || true

lint:
	black --check 08_Automation
	isort --check-only 08_Automation

format:
	black 08_Automation
	isort 08_Automation

sync:
	bash 08_Automation/sync_repos.sh

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.log" -delete
