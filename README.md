# kit-agentes-python

Plantilla para arrancar proyectos Python trabajando con un **equipo de agentes** en Claude Code:
Spec-Driven Development, reglas de equipo, hooks que las hacen cumplir y tooling moderno.

## Qué trae

| Pieza | Para qué |
|---|---|
| `docs/equipo.md` | Reglas del equipo (Siempre / Preguntá antes / Nunca). Iguales en todo proyecto |
| `CLAUDE.md` | Esqueleto del proyecto. Importa `docs/equipo.md` |
| `MEMORY.md`, `docs/constitution.md`, `docs/adr/` | Memoria, principios innegociables y decisiones de arquitectura |
| `.claude/agents/` | `coordinator`, `planner`, `implementer` y `reviewer` |
| `.claude/commands/` | `/sdd-*` (flujo completo) y `/feature` (cambios chicos) |
| `.claude/skills/` | `sdd` (cómo se escriben specs, planes y tareas) y `grill-me` (revisión de diseño) |
| `.claude/hooks/` | `solo_specs.py` (el planner solo escribe en `specs/`) y `proteger_main.py` (nada de commits en `main` ni `push --force`) |
| `pyproject.toml` | uv, pytest, ruff (con reglas de seguridad) y mypy estricto |

## Requisitos

- [uv](https://docs.astral.sh/uv/) (instala Python solo si hace falta) y Git.

## Arrancar un proyecto nuevo

1. En GitHub: **Use this template → Create a new repository**, y clonarlo.
2. `uv sync` y verificar que la plantilla está sana:
   `uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest`
3. Renombrar el proyecto en `pyproject.toml` y completar `CLAUDE.md` (Qué es, Stack, Arquitectura, Datos).
4. En Claude Code: `/sdd-constitution` → aprobar → primera spec con `/sdd-spec 001-nombre <idea>`
   o el flujo completo con `claude --agent coordinator`.

## Flujo

Spec → Clarificación → Plan y tareas → Implementación (una tarea por vez, rama `feat/NNN-nombre`) → Validación → PR a `main`.
