---
name: entorno-windows
description: Úsala al editar o generar archivos en Windows u OneDrive - finales de línea CRLF, BOM, espacios duros, archivos binarios (capturas, APK), carpetas de build bloqueadas por OneDrive, o cuando una edición falla con "string not found" sin motivo aparente.
---

# Cuidar el entorno Windows y OneDrive

## Finales de línea, BOM y caracteres invisibles

- Antes de una edición delicada, mirá el formato: `python -c "print(open('ARCHIVO','rb').read(300))"` muestra `\r\n`, BOM (`\xef\xbb\xbf`) y espacios duros (`\xc2\xa0`).
- Si la herramienta Edit falla con "string not found" y el texto parece igual, casi siempre es CRLF, un `\r` suelto o un carácter invisible. No reintentes a ciegas: leé los bytes.
- Ediciones largas o con caracteres raros: escribí un script `.py` en el scratchpad (con la herramienta Write, no con heredoc) que lea en bytes, reemplace y escriba en bytes conservando `\r\n`. Después revisá `git diff`.
- No escribas código Python dentro de un heredoc de Bash con `\n` o `\r` en strings: las capas de escape los convierten en saltos de línea reales y rompen el archivo.
- BOM y espacio duro dentro del código: escribilos como escape (`﻿`, ` `), nunca el carácter literal; las herramientas de edición los transforman.
- Mantené el formato que ya tiene el archivo. Si Git avisa "LF will be replaced by CRLF", es normal; no conviertas archivos enteros.

## Archivos binarios

- En PowerShell, `>` reescribe la salida como texto y corrompe binarios (PNG, APK, ZIP). Generá el archivo en destino y copialo (ej. Android: `adb shell screencap /sdcard/c.png` y `adb pull /sdcard/c.png`), o usá Bash.

## OneDrive

- Si un build falla con "not a regular file", "Cannot snapshot", "Access denied" o archivos que desaparecen: OneDrive tiene la carpeta tomada o en "solo en línea".
- Arreglo: detené el proceso de build (ej. `gradlew --stop`), quitá atributos con `attrib -r -p` sobre la carpeta de build y borrá SOLO las carpetas de build (nunca fuentes). Confirmá la ruta antes de borrar.
- Si pasa seguido, proponé al usuario marcar la carpeta del proyecto como "Mantener siempre en este dispositivo" o sacar las carpetas de build de OneDrive.
- Anotá en **Comandos** de `CLAUDE.md` el procedimiento que funcionó en este proyecto.
