# ADR 0001 — Codex como ayudante de los agentes de Claude

Estado: aceptada · Fecha: 2026-11-23

## Contexto
Los cuatro subagentes usaban el modelo de la sesión principal (Opus) y hacían todo el trabajo
mecánico (borradores, código repetitivo, revisión de diffs), lo que gastaba muchos tokens del plan
de Claude. El usuario además tiene un plan de Codex (OpenAI) que no se aprovechaba.

## Decisión
- Los subagentes usan modelos más baratos: Haiku el coordinator y Sonnet el resto.
- Los subagentes delegan lo mecánico en Codex con `codex exec` (skill `codex`): el planner, los
  borradores; el implementer, las tareas chicas; el reviewer, una primera revisión. Claude siempre
  revisa y decide.
- Codex comparte las reglas a través de `AGENTS.md` y la memoria a través de `MEMORY.md`.
- El planner recibe Bash, limitado por el hook `solo_codex.py` a `codex exec` con sandbox y `git status`.

## Alternativas descartadas
- **Codex como servidor MCP (`codex mcp-server`)**: ya no existe en las versiones actuales del CLI.
- **SDK de Python de Codex (`openai_codex`)**: suma una dependencia y código propio para algo que
  `codex exec` ya resuelve desde la terminal.
- **Que Codex haga la implementación completa**: la calidad y las reglas del equipo dependen de que
  Claude revise; Codex se queda con lo mecánico.

## Consecuencias
- Menos tokens de Claude por tarea; parte del costo pasa a la cuota de Codex.
- Hace falta instalar el Codex CLI y loguearse. Sin Codex, el flujo sigue funcionando igual que antes.
- El sandbox de Codex no limita la escritura a `specs/`: el planner lo comprueba con `git status`
  después de cada borrador.
