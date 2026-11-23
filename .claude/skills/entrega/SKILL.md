---
name: entrega
description: Úsala al cerrar una spec o una parte - preparar el PR y una guía de prueba paso a paso, en español, para que un usuario no técnico pruebe y apruebe por partes.
---

# Preparar una entrega

- Si **Comandos** de `CLAUDE.md` no tiene el comando que necesitás, preguntá al usuario y, con su respuesta, proponé agregarlo ahí. No lo inventes.
- Leé `MEMORY.md`, la spec y sus tareas, `docs/` relevante y la sección **Comandos** de `CLAUDE.md`.
- Confirmá qué partes están listas, cuáles requieren prueba externa y qué límites siguen abiertos.
- Prepará la descripción del PR en español, breve y concreta. Incluí:
  - objetivo y resumen de los cambios visibles para quien los usa;
  - alcance por parte y qué queda fuera;
  - verificaciones automáticas y manuales, con resultados reales;
  - cómo obtener o instalar la versión de prueba, si aplica, remitiendo a las instrucciones del proyecto;
  - guía de prueba numerada, con una acción por paso y el resultado esperado en palabras simples;
  - limitaciones conocidas, riesgos prácticos y archivos o enlaces útiles.
- Separá cada parte para que se pueda revisar y aprobar de manera independiente. No presentes como probado lo que solo se simuló.
- Para cada paso, indicá cómo informar «funcionó», «falló» o «no pude probarlo» y qué dato adjuntar, sin pedir información sensible.
- Registrá la aprobación con fecha, parte aprobada, versión o PR probado y quién la dio, en el documento de seguimiento del proyecto. Si no existe, proponé la ruta en la entrega.
- No marques una parte aprobada por silencio, por pruebas automáticas ni por aprobación de otra parte.
- Dejá el PR listo para revisión; seguí las reglas del proyecto para crear, publicar o fusionar PR.
- Usá los comandos concretos solo desde **Comandos** de `CLAUDE.md`.