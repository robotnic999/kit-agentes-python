---
description: SDD · Valida la spec RF por RF (tests + Chrome DevTools)
---
Recorre specs/$0/spec.md requisito por requisito. Para cada RF indica qué test
lo cubre y el resultado de ejecutarlo con uv run pytest. Corre también la
verificación completa de CLAUDE.md (ruff y mypy).
Los RF que no se puedan testear automáticamente, verifícalos como indique
CLAUDE.md (por ejemplo, con el navegador si hay interfaz).
Si algún RF no está cubierto o falla, dilo claramente. NO arregles nada todavía.
Después comprueba los criterios de finalización y dame un veredicto:
¿la spec está cumplida?
