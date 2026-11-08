---
description: SDD · Genera el plan técnico de una spec aprobada
---
Lee docs/constitution.md, CLAUDE.md y specs/$0/spec.md. Usa la skill sdd.
NO escribas código.
Genera specs/$0/plan.md con: archivos que se crean o modifican y la
responsabilidad de cada uno, dónde vive la lógica de negocio (sin depender de
frameworks, base de datos ni reloj), algoritmo en pseudocódigo, contratos
(endpoints, esquemas y errores), decisiones técnicas justificadas (con su
alternativa descartada, y si hace falta un ADR) y estrategia de tests con pytest.
Todo debe respetar la constitución y cubrir todos los RF. Marca qué RF cubre
cada parte. Si la spec no está aprobada o tiene dudas abiertas, para y avísame.
