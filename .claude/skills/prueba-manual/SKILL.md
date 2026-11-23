---
name: prueba-manual
description: Úsala cuando algo solo se puede comprobar en un dispositivo o hardware real (celular, tablet, impresora, sensor) - checklist de prueba, registro de resultados y separar lo probado de verdad de lo simulado.
---

# Prueba manual

- Si **Comandos** de `CLAUDE.md` no tiene el comando que necesitás, preguntá al usuario y, con su respuesta, proponé agregarlo ahí. No lo inventes.
- Leé la spec, las tareas, las guías de uso y la sección **Comandos** de `CLAUDE.md`.
- Prepará un checklist breve, ordenado y apto para quien no conoce la implementación.
- Para cada caso anotá: requisito o parte, preparación, acción, resultado esperado y resultado observado.
- Indicá el dispositivo real, modelo o entorno, versión relevante, compilación probada y fecha. Omití datos personales y secretos.
- Marcá cada caso como **probado en dispositivo**, **simulado**, **no probado** o **bloqueado**. No mezcles esos estados.
- Registrá errores con pasos para reproducir, frecuencia, resultado esperado y evidencia disponible; ocultá credenciales y datos privados.
- Guardá el registro en un archivo de `docs/`, siguiendo el nombre y formato existentes. Si no hay convención, elegí un nombre descriptivo y enlazalo desde la entrega.
- Anotá qué escenarios no se pudieron ejecutar y por qué; no los conviertas en aprobados.
- Al cerrar, resumí resultados por parte y pedí aprobación explícita de cada parte al responsable definido por el proyecto.
- Usá los comandos concretos solo desde **Comandos** de `CLAUDE.md`.