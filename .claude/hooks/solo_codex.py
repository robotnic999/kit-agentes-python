"""Hook PreToolUse de Bash del agente planner: solo deja usar Codex y `git status`.

El planner usa Bash únicamente para delegar el borrador en Codex (`codex exec ...`)
y para comprobar después qué archivos tocó (`git status`). Al final se acepta
`2>/dev/null`, para descartar el progreso de Codex y leer solo su respuesta.
Se bloquea (código 2):
- cualquier otro comando;
- encadenar o redirigir comandos (`&&`, `;`, `|`, `>`, …) o sustituirlos (`$(…)`, backticks);
- los modos de Codex sin sandbox.
Es una red de seguridad, no un control perfecto.
"""

import json
import shlex
import sys

OPERADORES = {";", "&&", "||", "|", "&", ">", ">>", "<", "<<", "|&", ";;", "(", ")"}
DESCARTAR_PROGRESO = "2>/dev/null"
FLAGS_PROHIBIDAS = {
    "danger-full-access",
    "--sandbox=danger-full-access",
    "--dangerously-bypass-approvals-and-sandbox",
    "--yolo",
}


def motivo_de_bloqueo(comando: str) -> str | None:
    """Devuelve por qué se bloquea el comando, o None si está permitido."""
    comando = comando.strip().removesuffix(DESCARTAR_PROGRESO)
    if "\n" in comando or "\r" in comando:
        return "el comando tiene que ir en una sola línea"
    if "$(" in comando or "`" in comando:
        return "no se permite sustituir comandos"
    lexer = shlex.shlex(comando, posix=True, punctuation_chars=True)
    lexer.whitespace_split = True
    try:
        palabras = list(lexer)
    except ValueError:
        return "comando mal formado"
    if any(palabra in OPERADORES for palabra in palabras):
        return "no se permite encadenar ni redirigir comandos"
    if palabras[:2] == ["git", "status"]:
        return None
    if palabras[:2] != ["codex", "exec"]:
        return "solo se permite `codex exec …` y `git status`"
    if any(palabra in FLAGS_PROHIBIDAS for palabra in palabras):
        return "Codex tiene que correr con sandbox (read-only o workspace-write)"
    return None


def main() -> int:
    datos = json.load(sys.stdin)
    comando = (datos.get("tool_input") or {}).get("command") or ""
    motivo = motivo_de_bloqueo(comando)
    if motivo is None:
        return 0
    print(f"Bloqueado para el planner: {motivo} ({comando}).", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
