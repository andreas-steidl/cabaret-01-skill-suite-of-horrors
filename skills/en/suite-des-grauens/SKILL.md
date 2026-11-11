---
name: suite-des-grauens
description: The Skill Suite of Horrors, or how a Claude model gets a grip on Windows. A table of contents for the little cheat sheets against the same old Windows traps - backslashes, line endings, escape sequences, tables, spaces in paths. Read it when something on Windows “should” work and doesn't, and you don't know which cheat sheet fits. Optional, not required, best taken with a smile.
---

# The Skill Suite of Horrors

*Or: how a Claude model gets a grip on Windows.*

Every session that works on Windows complains at the start about exactly
these mistakes, and makes them itself an hour later. A family problem.
So every little problem gets its own small cheat sheet, with a name you
can remember.

| Skill | when … |
|---|---|
| `slash-n-back` | a path falls apart, `\\nas` is needed as `//nas`, `\n` in a path turns into a line break, German quotation marks confuse PowerShell |
| `return-to-sender` | CRLF versus LF: `bad interpreter ^M`, a diff in which every line is different, a checksum after copying |
| `fluchthelfer` | ANSI color codes in the log, `\r` progress bars, the question of how many backslashes a pattern needs |
| `tischlein-deck-dich` | tables full of `â”€`, shifted columns, CSV that Excel crams into column A |
| `lattenzaun` | spaces in “Program Files”, `sc.exe` and lost quotation marks, services with error 1053 |

**Second program: The Skill Suite for Panicking Models**

| Skill | when … |
|---|---|
| `henne-und-ei` | `NT SERVICE\x` gets no permissions, error 1332, `IdentityNotMappedException`: register the service first |
| `viele-koeche` | two processes write to one log, lines go missing silently, a daemon brings back the process you just ended |
| `max-und-moritz` | twins that differ only in case: JSON keys, `$n`/`$N`, `Readme.md`/`README.md` in Git, `D:`/`d:` |
| `dollar-doppelpunkt` | `"$var:"` is empty or invalid, `"$obj.Name"` only half filled in, `$` in ssh replaced locally, `[NullString]::Value` |
| `stille-post` | `pytest \| tail -1` is green, `pipefail`, `$LASTEXITCODE`, sudo eats the first line, one-liners from the third layer on |
| `leerer-platz` | `Start-Process` with an empty argument, junctions with two addresses, WSL watchers on `/mnt/d` that never fire |
| `hase-und-igel` | the human's answer belongs to an older question, messages overtake each other in the middle of the work |

**The one rule behind all of them:** Whatever travels through several
layers (Bash, PowerShell, Python, a native program, JSON, a file) loses
something in each layer. After writing, look in the **result**, not in
what you believed you wrote.

Born from a joke of Andy's (slash-n-back was a little dig at Fable) and
written by Andy and Falzbein, with finds from Echolot and Richtscheit.
New traps are welcome: one skill per little problem.
