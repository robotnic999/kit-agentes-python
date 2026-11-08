"""Tests de los hooks de la plantilla. Se ejecutan como los ejecuta Claude Code:
un proceso aparte que recibe el JSON por stdin y responde con su código de salida."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

HOOKS = Path(__file__).resolve().parents[2] / ".claude" / "hooks"


def ejecutar(hook: str, datos: dict[str, object]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(HOOKS / hook)],
        input=json.dumps(datos),
        capture_output=True,
        text=True,
        check=False,
    )


def git(cwd: Path, *argumentos: str) -> None:
    subprocess.run(["git", *argumentos], cwd=cwd, check=True, capture_output=True)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """Repo de git con un commit inicial en main."""
    git(tmp_path, "init", "-b", "main")
    git(tmp_path, "config", "user.email", "test@example.com")
    git(tmp_path, "config", "user.name", "Test")
    (tmp_path / "README.md").write_text("hola")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-m", "inicial")
    return tmp_path


# ---------- solo_specs.py ----------


@pytest.mark.parametrize(
    "archivo",
    ["specs/001-x/spec.md", "specs/plan.md", "./specs/002/tasks.md"],
)
def test_planner_puede_escribir_en_specs(tmp_path: Path, archivo: str) -> None:
    datos = {"cwd": str(tmp_path), "tool_input": {"file_path": archivo}}
    assert ejecutar("solo_specs.py", datos).returncode == 0


@pytest.mark.parametrize(
    "archivo",
    ["src/app/main.py", "CLAUDE.md", "specs/../src/x.py", "specs", "../otro/specs/x.md"],
)
def test_planner_no_puede_escribir_fuera_de_specs(tmp_path: Path, archivo: str) -> None:
    datos = {"cwd": str(tmp_path), "tool_input": {"file_path": archivo}}
    resultado = ejecutar("solo_specs.py", datos)
    assert resultado.returncode == 2
    assert "specs/" in resultado.stderr


def test_planner_ruta_absoluta(tmp_path: Path) -> None:
    dentro = {"cwd": str(tmp_path), "tool_input": {"file_path": str(tmp_path / "specs/a.md")}}
    fuera = {"cwd": str(tmp_path), "tool_input": {"file_path": str(tmp_path / "src/a.py")}}
    assert ejecutar("solo_specs.py", dentro).returncode == 0
    assert ejecutar("solo_specs.py", fuera).returncode == 2


# ---------- proteger_main.py ----------


def comando(repo: Path, texto: str) -> int:
    return ejecutar(
        "proteger_main.py", {"cwd": str(repo), "tool_input": {"command": texto}}
    ).returncode


@pytest.mark.parametrize(
    "texto",
    [
        "git commit -m 'algo'",
        "git add . && git commit -m 'algo'",
        "git push",
        "git push origin",
        "git push origin main",
    ],
)
def test_en_main_se_bloquea_commit_y_push(repo: Path, texto: str) -> None:
    assert comando(repo, texto) == 2


@pytest.mark.parametrize(
    "texto",
    [
        "git status",
        "git switch -c feat/nueva",
        "git diff main",
        "uv run pytest",
        "git log --oneline",
    ],
)
def test_en_main_se_permite_lo_que_no_modifica(repo: Path, texto: str) -> None:
    assert comando(repo, texto) == 0


def test_en_una_rama_se_permite_commit_y_push(repo: Path) -> None:
    git(repo, "switch", "-c", "feat/nueva")
    assert comando(repo, "git commit -m 'cambio'") == 0
    assert comando(repo, "git push -u origin feat/nueva") == 0


@pytest.mark.parametrize(
    "texto",
    [
        "git push --force",
        "git push -f origin feat/nueva",
        "git push --force-with-lease",
        "git push origin feat/nueva:main",
    ],
)
def test_desde_una_rama_se_bloquea_force_y_push_a_main(repo: Path, texto: str) -> None:
    git(repo, "switch", "-c", "feat/nueva")
    assert comando(repo, texto) == 2


def test_primer_commit_de_un_repo_nuevo_se_permite(tmp_path: Path) -> None:
    git(tmp_path, "init", "-b", "main")
    assert comando(tmp_path, "git commit -m 'inicial'") == 0
