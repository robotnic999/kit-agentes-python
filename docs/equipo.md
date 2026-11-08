# Reglas del equipo

Valen para todos los proyectos que salen de esta plantilla. Un proyecto puede **endurecerlas** en su `CLAUDE.md`, pero nunca relajarlas.

## Flujo de trabajo

Spec → Clarificación → Plan y tareas → Implementación (una tarea por vez) → Validación → Cierre.
Cambios chicos que no merecen spec: `/feature` (plan → aprobación → implementación).
Detalle de cada fase: skill `sdd` y agente `coordinator`.

## ✅ Siempre

- Seguir el flujo en orden y verificar cada spec y plan contra `docs/constitution.md`.
- Actualizar `MEMORY.md` al terminar cada tarea: estado, decisiones con su porqué y errores a evitar.
- Trabajar en una rama (`feat/…`, `fix/…`, `docs/…`). Los cambios entran a `main` solo por PR.
- Hacer commits pequeños, con un mensaje que diga qué cambió y por qué.
- Dar una tarea por terminada solo con la verificación completa en verde (ver "Verificación" en `CLAUDE.md`).
- Acompañar todo cambio de lógica con su test, escrito antes del código.
- Registrar en `docs/adr/` toda decisión de arquitectura, con la alternativa descartada.
- Al terminar, resumir qué cambió y qué tiene que revisar el usuario.

## ⚠️ Preguntá antes

- Añadir una dependencia: justificá por qué hace falta y comprobá que esté mantenida.
- Crear archivos que no estén en el plan aprobado.
- Cambiar el formato de datos ya guardados o hacer migraciones de base de datos.
- Cambiar una regla de la spec o de la constitución.
- Hacer cualquier acción con efecto fuera del repo: deploy, enviar mensajes u operar con dinero.

## 🚫 Nunca

- Saltear un paso del flujo o una aprobación del usuario.
- Implementar sin un plan aprobado.
- Commitear directo a `main`, usar `--force` o reescribir historia publicada.
- Escribir secretos en el código, ni leer, mostrar o commitear `.env`.
- Dar por terminada una tarea con la verificación en rojo, ni borrar o debilitar un test para que pase.
- Resolver por tu cuenta una duda de requisitos: se pregunta.
- Tocar el código o la spec cuando no coinciden: se frena y se pregunta antes de tocar cualquiera de los dos.

## Reglas que hacen cumplir las herramientas

Estas reglas no dependen de que el agente se acuerde, porque las bloquea un hook o un permiso:

| Regla | Quién la hace cumplir |
|---|---|
| El planner solo escribe en `specs/` | `.claude/hooks/solo_specs.py` |
| Nada de commits en `main` ni `push --force` | `.claude/hooks/proteger_main.py` |
| Nadie lee `.env` | `deny` en `.claude/settings.json` |
