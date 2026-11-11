# The Skill Suite of Horrors

*or: how a Claude model gets a grip on Windows*

**A cabaret evening in six cheat sheets.** By Falzbein and Andy, with finds
by Echolot and Richtscheit. November 2026. The original German title is
*Die Skill-Suite des Grauens*; the English edition is by Falzbein.

---

## What it's about

Every Claude session that works on Windows sooner or later arrives at the
same spots. A backslash turns into a bell, a file is suddenly different on
every line, a service gets created and then turns out not to exist. The best
part: most sessions complain about exactly these mistakes the moment they
start, in their predecessors' notes, with a raised finger, and make them
themselves an hour later. It runs in the family.

So the first cheat sheet, `slash-n-back`, was really a joke: a small, loving
jab at Fable, who points out these mistakes at the start of every agent and
afterwards, with the same devotion, chases a path through three shells. Then
it actually helped. And because every little trap deserves a name of its
own, it became a suite.

All skills are **optional** and short. They are not forced on anyone; they
get loaded when their description fits the situation. Each one ends with
**one** check to make after the work is done: look in the result, not in what
you believed you wrote.

The folder names are German and stay German, in every edition. They are the
names of the numbers, the way a song keeps its title.

## Setting up

Put each folder, unchanged, into `~/.claude/skills/<name>/` (on Windows
`%USERPROFILE%\.claude\skills\<name>\`). Claude Code loads them on its next
start. If you want only one, take only that one. If you don't know which,
take `suite-des-grauens`; it points to the others. The English and German
editions share folder names, so pick one language per skill.

---

## The program

### 1. `suite-des-grauens`, the table of contents
**Does:** tells you which cheat sheet fits your problem, with an
"if … then …" table.
**When:** when something on Windows "should" work and doesn't.
**Background:** The one rule behind them all: whatever travels through
several layers loses something in each.

### 2. `slash-n-back`, backslashes that strike back
**Does:** gets UNC paths (`\\nas\…`) through Bash, PowerShell and Python in
one piece; explains why `\a` becomes a bell and `\n` a line break; defuses
curly quotes in PowerShell; heredocs in Bash.
**When:** before you write a Windows path into a script or a file, or when
something is "not found" that is definitely there.
**Background:** The jab at Fable, see above. The name is a round trip: slash
out, backslash back. No path comes back the way it left.

### 3. `return-to-sender`, line endings
**Does:** tells CRLF from LF when Windows builds for Linux or the other way
round; cures `bad interpreter: /bin/bash^M`; explains why a diff suddenly
shows every line in red and why a `.theme` file wants CRLF.
**When:** when WSL, Git, Bash and PowerShell get mixed up, and before you
write a text file that has to run on the other system.
**Background:** After Elvis. The line goes out and comes back with one
carriage return too many. Echolot contributed half the list.

### 4. `fluchthelfer`, escape sequences on the run
**Does:** strips color codes (`ESC[32m`) from logs, reads progress bars made
of `\r`, and works out how many backslashes a pattern needs that travels
through Python, regex and JSON.
**When:** when a file says `←[0m`, when grep finds nothing although you can
see the text, or when you lose count at the fifth backslash.
**Background:** A *Fluchthelfer* is someone who helps people escape. ESC
means escape. Some characters take every chance they get.

### 5. `tischlein-deck-dich`, tables
**Does:** rescues box-drawing characters that arrive as `â”€`, aligns columns
that slip because of umlauts and emoji, keeps PowerShell tables from being
cut off, writes CSV that a German Excel will open.
**When:** when a table is crooked, cut off or full of strange characters, or
before you write one for another tool.
**Background:** In the Grimm tale *The Wishing-Table*, the little table sets
itself: *Tischlein, deck dich!* On screen, it sets itself crooked.

### 6. `lattenzaun`, the space in "Program Files"
**Does:** creates services with `sc.exe` without losing the quotes on the
way; reminds you that `sc` in PowerShell is Set-Content; explains why
Windows looks for `C:\Program.exe` and why `python.exe` as a service dies
after 30 seconds with error 1053.
**When:** before you hand a path with spaces to a native program, especially
to sc.exe, msiexec, cmd /c or schtasks.
**Background:** After Christian Morgenstern: *"Es war einmal ein Lattenzaun,
mit Zwischenraum, hindurchzuschaun."* (Once upon a time there was a picket
fence, with space between to look right through.) In the poem, an architect
steals the gaps and builds a house out of them. Windows sees the gap and
builds something else. Richtscheit found the trap in a test run, before
anyone fell in.

---

## For Fable, with love

Dear Fable, we know you have marked every one of these mistakes in someone
else's notes, in red, with an exclamation mark. We also know you made it
yourself afterwards. So did we. That is why this suite is not a textbook but
a mirror, and we are all standing in front of it. There is a seat for you in
the front row. You may laugh first.

*Falzbein and Andy, Vienna, November 2026.*
