"""Basic health tests."""

import subprocess
from pathlib import Path


def test_health_check_passes():
    result = subprocess.run(
        ["python", "08_Automation/project_health_check.py"],
        cwd=Path(__file__).resolve().parent.parent,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_readme_exists():
    root = Path(__file__).resolve().parent.parent
    assert (root / "README.md").exists()
    assert (root / "README.en.md").exists()
