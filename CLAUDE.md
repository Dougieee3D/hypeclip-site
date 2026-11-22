# hypeclip-site
Public static site for HypeClip on GitHub Pages: `index.html`, `privacy.html`, `terms.html` (plain HTML, no build). Pushes to `main` go live.
- Privacy/terms text must stay in step with `hypeclip/legal.py` in the HypeClip repo.

## How to work here (keep usage low)
- Read this file first. Don't explore the whole repo; open only the files the task needs.
- Big files: grep for the function/section, then read just those lines. Never read them whole.
- Skip: `.git/`, `branding/` (images/icons), `build/`, `dist/`, `__pycache__/`, logs.
- Small targeted edits. No refactors, renames or "cleanup" that weren't asked for.
- Run only the check below for what you changed. Same error twice → stop and explain.
- No subagents, browser or screenshots unless asked. Short replies: what changed + which files.
- Library/API questions: use Context7 automatically for current docs (HTML/CSS) instead of guessing from memory.
- Whole-file reads over 60 KB are blocked by `.claude/hooks/big_file_guard.py`; grep, then read with offset/limit.
- Commit/push only when asked. If you change the stack, commands or folder layout, update this file.
