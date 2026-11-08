# CLAUDE.md — <Nombre del proyecto>

<!-- PLANTILLA: completá cada sección y borrá los comentarios. Lo que no aplique, borralo. -->

@docs/equipo.md

## Qué es

<!-- 2-3 líneas: qué problema resuelve, para quién y qué NO es. -->

## Stack y estructura

- Python 3.12+, gestionado con `uv`. <!-- Agregá: framework (FastAPI…), base de datos, servicios externos. -->
- `src/app/`: código de la aplicación. <!-- Describí cada módulo y su responsabilidad. -->
- `tests/`: tests con pytest. `tests/kit/` testea los hooks de la plantilla: no borrar.
- `specs/`: specs SDD (`NNN-nombre/spec.md`, `plan.md`, `tasks.md`).
- `docs/`: `constitution.md`, `equipo.md` y `adr/` (decisiones de arquitectura).

## Arquitectura

<!-- Capas o puertos y adaptadores, qué depende de qué. Enlazá los ADR relevantes. -->

## Convenciones

- Código y nombres en <!-- español | inglés -->. Textos para el usuario en <!-- idioma / registro -->.
- Formato y lint: ruff (la configuración está en `pyproject.toml`). Tipos: mypy en modo estricto sobre `src/`.
- Funciones con type hints. La lógica de negocio no depende de frameworks ni de la base de datos.
<!-- Agregá las convenciones del proyecto. -->

## Datos

<!-- Dónde se guardan, formato y esquema, y qué no se puede romper. -->

## Reglas propias del proyecto

<!-- Reglas que endurecen docs/equipo.md para este proyecto. Ej.: "🚫 Nunca: añadir dependencias". -->

## Comandos

- Instalar: `uv sync`
- Tests: `uv run pytest`
- Lint y formato: `uv run ruff check .` y `uv run ruff format .`
- Tipos: `uv run mypy`

## Verificación (la tarea no está terminada sin esto en verde)

```
uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest
```

## Memoria

- Al empezar, leé `MEMORY.md` (estado del proyecto y decisiones tomadas).
- Al terminar una tarea, actualizalo: estado actual, decisiones con su porqué y errores a evitar.
- Máximo unas 50 líneas: resumí o eliminá lo que ya no aporte.
- Si algo se vuelve regla permanente, proponé moverlo a `CLAUDE.md`.
- Nunca guardes datos sensibles (claves, tokens, datos personales).
