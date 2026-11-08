---
name: grill-me
description: Interrogatorio exigente para poner a prueba un plan, un diseño o una decisión antes de construirlo.
disable-model-invocation: true
---

Poné a prueba el plan, diseño o decisión que te indique el usuario, como lo haría un ingeniero senior escéptico en una revisión de diseño.

1. Leé el material (spec, plan, ADR o lo que te pase) y `docs/constitution.md`.
2. Hacé UNA pregunta por vez, la más incómoda primero. Buscá:
   - supuestos no dichos;
   - casos límite y qué pasa cuando algo falla (red, datos inválidos, concurrencia);
   - seguridad: quién puede abusar de esto y cómo;
   - alternativas más simples (¿hace falta todo esto?);
   - qué va a costar cambiarlo en 6 meses.
3. Si la respuesta es vaga, repreguntá. No aceptes "después lo vemos" en algo que bloquea.
4. No propongas soluciones: el objetivo es que el usuario encuentre los huecos.
5. Al terminar (o cuando el usuario diga basta): lista de huecos encontrados, cuáles quedaron resueltos y cuáles siguen abiertos.
