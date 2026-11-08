"""Hook PreToolUse del agente planner: bloquea cualquier escritura fuera de specs/.

Claude Code manda por stdin un JSON con la herramienta y la ruta del archivo.
Salir con código 2 bloquea la acción y el texto de stderr le llega al agente.
"""

import json
import os
import sys
from pathlib import Path


def esta_dentro_de_specs(archivo: str, raiz: str) -> bool:
    carpeta_specs = (Path(raiz) / "specs").resolve()
    destino = (Path(raiz) / archivo).resolve()  # si `archivo` es absoluto, se ignora `raiz`
    return destino != carpeta_specs and destino.is_relative_to(carpeta_specs)


def main() -> int:
    datos = json.load(sys.stdin)
    archivo = (datos.get("tool_input") or {}).get("file_path")
    if not archivo:
        return 0

    raiz = os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd") or "."
    if esta_dentro_de_specs(archivo, raiz):
        return 0

    print(
        f"Bloqueado: el planner solo puede escribir dentro de specs/ ({archivo}).", file=sys.stderr
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
