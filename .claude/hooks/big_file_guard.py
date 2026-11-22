"""Claude Code hook: stop whole-file reads of big files so Claude searches instead.

Reads over LIMIT_KB without offset/limit are denied with a short hint. Partial
reads (offset/limit) always pass. Never blocks anything else; on any error it allows.
"""
import json, os, sys

LIMIT_KB = 60

def main():
    try:
        data = json.load(sys.stdin)
        inp = data.get("tool_input") or {}
        path = inp.get("file_path") or ""
        if not path or inp.get("offset") is not None or inp.get("limit") is not None:
            return
        if not os.path.isfile(path):
            return
        kb = os.path.getsize(path) // 1024
        if kb <= LIMIT_KB:
            return
        reason = (f"{os.path.basename(path)} is {kb} KB. Don't read it whole: Grep for the "
                  "function/section first, then Read with offset and limit (about 150 lines).")
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason}}))
    except Exception:
        return

if __name__ == "__main__":
    main()
