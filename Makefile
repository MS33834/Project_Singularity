.PHONY: help check setup docker test lint format sync clean

help:
	@echo "Project Singularity — Common commands"
	@echo "  make check     Verify project structure"
	@echo "  make setup     Install dev dependencies (includes black, isort, pytest)"
	@echo "  make docker    Start Docker container"
	@echo "  make test      Run health check, linters, pytest, preflight"
	@echo "  make lint      Run linters (black, isort)"
	@echo "  make format    Auto-format code"
	@echo "  make sync      Push to GitHub and GitCode"
	@echo "  make clean     Remove temp files"

check:
	python 08_Automation/project_health_check.py

setup:
	pip install -r 08_Automation/requirements-dev.txt

docker:
	docker compose up -d

test: check lint
	pytest
	python 08_Automation/preflight_check.py || true

lint:
	black --check 08_Automation tests
	isort --check-only 08_Automation tests

format:
	black 08_Automation tests
	isort 08_Automation tests

sync:
	bash 08_Automation/sync_repos.sh

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.log" -delete
