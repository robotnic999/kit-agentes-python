"""Hook PreToolUse de Bash: hace cumplir las reglas de Git del equipo.

Bloquea (código de salida 2):
- `git commit` mientras la rama actual es main o master (salvo el primer commit del repo).
- `git push` a main o master, o cualquier push con --force / -f.
Las reglas están en docs/equipo.md. Es una red de seguridad, no un control perfecto:
un comando muy rebuscado podría esquivarla.
"""

import json
import re
import subprocess
import sys

RAMAS_PROTEGIDAS = {"main", "master"}


def rama_actual(cwd: str) -> str | None:
    """Rama actual, o None si el repo todavía no tiene commits (o no es un repo)."""
    resultado = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    if resultado.returncode != 0:
        return None
    return resultado.stdout.strip()


def motivo_de_bloqueo(comando: str, rama: str | None) -> str | None:
    """Devuelve por qué se bloquea el comando, o None si está permitido."""
    for parte in re.split(r"&&|\|\||;|\n", comando):
        palabras = parte.split()
        if len(palabras) < 2 or palabras[0] != "git":
            continue
        subcomando, argumentos = palabras[1], palabras[2:]

        if subcomando == "commit" and rama in RAMAS_PROTEGIDAS:
            return f"no se commitea en '{rama}'. Creá una rama: git switch -c feat/<nombre>"

        if subcomando == "push":
            if any(a in ("--force", "-f") or a.startswith("--force") for a in argumentos):
                return "push --force está prohibido (reescribe historia publicada)"
            destinos = {a.split(":")[-1] for a in argumentos if not a.startswith("-")}
            if destinos & RAMAS_PROTEGIDAS:
                return "no se pushea directo a main: los cambios entran por PR"
            if not destinos - {"origin"} and rama in RAMAS_PROTEGIDAS:
                return f"estás en '{rama}': los cambios entran por PR desde una rama"
    return None


def main() -> int:
    datos = json.load(sys.stdin)
    comando = (datos.get("tool_input") or {}).get("command") or ""
    if "git" not in comando:
        return 0

    motivo = motivo_de_bloqueo(comando, rama_actual(datos.get("cwd") or "."))
    if motivo is None:
        return 0

    print(f"Bloqueado por las reglas del equipo: {motivo}.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
