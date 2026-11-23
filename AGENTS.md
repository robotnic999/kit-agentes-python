# AGENTS.md — instrucciones para Codex

Trabajás en equipo con Claude Code: Claude coordina y decide, vos hacés el trabajo mecánico que te
encarga. Las reglas son las mismas para los dos y viven en estos archivos (leelos antes de empezar):

- `CLAUDE.md`: stack, convenciones, comandos y verificación del proyecto.
- `docs/equipo.md`: reglas del equipo (siempre / preguntá antes / nunca).
- `docs/constitution.md`: principios innegociables.
- `MEMORY.md`: estado actual, decisiones y errores a evitar.
- `.claude/skills/sdd/SKILL.md`: formato de specs, planes y tareas.

## Reglas para vos

- Hacé SOLO lo que dice el encargo y tocá solo los archivos que te permite.
- No hagas commits, push ni nada fuera del repo. No leas ni toques `.env`.
- Si algo del encargo es ambiguo o contradice la spec, no lo resuelvas: anotalo como duda en tu respuesta.
- Tests primero en la lógica. Nunca borres ni debilites un test.
- Respondé corto (5 líneas como máximo, salvo que el encargo pida otra cosa): qué hiciste, qué
  archivos cambiaste y qué dudas quedan.
- Si aprendés algo que le sirva al equipo, ponelo en tu respuesta; Claude decide si va a `MEMORY.md`.
