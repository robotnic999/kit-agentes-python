# MEMORY.md — <Nombre del proyecto>

Memoria del proyecto entre sesiones. Máximo unas 50 líneas: resumí o eliminá lo que ya no aporte.

## Estado actual

- Proyecto creado desde `kit-agentes-python`. Falta: completar `CLAUDE.md` y crear la constitución (`/sdd-constitution`).

## Decisiones (y por qué)

- Codex hace lo mecánico (borradores, tareas chicas, primera revisión) y los subagentes usan Sonnet/Haiku: ahorra tokens de Claude. Ver `docs/adr/0001-codex-como-ayudante.md`.

## Aprendizajes y errores a evitar

- Skills `entrega`, `prueba-manual`, `capturas` y `entorno-windows` salieron de lo aprendido en el proyecto App tablet (borrador de Codex, revisado por Claude).
- Python con `\n` dentro de un heredoc de Bash rompe archivos: usar un script `.py` (ver skill `entorno-windows`).

## Entorno

- Codex CLI: `npm install -g @openai/codex` y `codex login`. Si no está, los agentes siguen sin él.
