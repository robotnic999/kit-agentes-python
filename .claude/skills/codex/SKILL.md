---
name: codex
description: Delegar trabajo mecánico en Codex (OpenAI) para ahorrar tokens de Claude - borradores de spec y plan, tareas chicas de código y primera revisión de un diff. Úsala desde planner, implementer y reviewer.
---

# Trabajar con Codex

Codex es un segundo agente que corre con la cuenta de OpenAI del usuario. Le delegamos lo mecánico
para que Claude gaste tokens solo en decidir y revisar. **Codex propone, Claude decide**: nada de lo
que hace Codex se da por bueno sin revisarlo.

Codex lee `AGENTS.md` (las mismas reglas que `CLAUDE.md`) y `MEMORY.md`, así que no hace falta
repetirle el contexto del proyecto en cada encargo.

## Antes de usarlo

- Si `codex` no existe, falla el login o se quedó sin cuota: seguí sin Codex y avisalo en una línea
  en tu respuesta. Nunca intentes instalarlo ni loguearte vos.
- Agregá siempre `2>/dev/null` al final: descarta el progreso de Codex y te deja solo su respuesta
  final (así leés menos).
- Nunca uses `--sandbox danger-full-access`, `--yolo` ni `--dangerously-bypass-approvals-and-sandbox`.

## Cómo escribir el encargo

Corto y autocontenido, en español, con:

1. Qué hacer, en una o dos frases.
2. Las rutas que tiene que leer (no pegues su contenido).
3. Qué archivos puede tocar y cuáles no.
4. En una sola línea, sin backticks ni `$(`: el hook del planner bloquea el comando si los ve.
5. Qué tiene que devolver: "Respondé en 5 líneas como máximo: qué archivos cambiaste y qué dudas quedan."

## Recetas

### Borrador (planner)

```bash
codex exec --sandbox workspace-write "Redactá specs/003-x/spec.md siguiendo .claude/skills/sdd/SKILL.md y docs/constitution.md. Pedido del usuario: <sus palabras y respuestas>. Solo podés escribir dentro de specs/003-x/. Respondé en 5 líneas: archivos y dudas." 2>/dev/null
```

Después: `git status --porcelain`. Si aparece algo fuera de `specs/`, FRENÁ y avisalo (no lo
deshagas vos). Leé el borrador y corregí solo lo necesario.

### Tarea chica (implementer)

```bash
codex exec --sandbox workspace-write "Tarea T2 de specs/003-x/tasks.md. Leé su plan.md. Primero el test, después el código. Tocá solo <archivos>. No hagas commit. Respondé en 5 líneas." 2>/dev/null
```

Después: `git diff` de lo que cambió, la verificación completa de `CLAUDE.md`, y el commit lo hacés vos.

### Revisión (reviewer)

```bash
codex exec review --base main 2>/dev/null
```

(`--uncommitted` para cambios sin commitear.) Cada hallazgo de Codex es una pista, no un veredicto:
comprobalo en el código y descartá lo que no se confirme. El veredicto lo da el reviewer.

## Qué NO delegar

- Decisiones de requisitos o de arquitectura, y cualquier duda del usuario.
- Commits, push, PR, o cualquier acción fuera del repo.
- Leer o tocar `.env` o secretos.
