# The Skill Suite of Horrors

*or: how a Claude model gets a grip on Windows* · German: *Die Skill-Suite des Grauens*

The first season of a small cabaret by Falzbein and Andy: six short, optional cheat sheets
(Claude Code skills) against the Windows traps every session walks into sooner or later —
backslashes that turn into bells, line endings, escape sequences, tables that fall apart,
and spaces in "Program Files". Each sheet ends with one check you do on the result.
Website: https://grauen.special.at/

| skill (folder) | English title |
|---|---|
| `suite-des-grauens` | table of contents |
| `slash-n-back` | slash-n-back |
| `return-to-sender` | return-to-sender |
| `fluchthelfer` | houdini |
| `tischlein-deck-dich` | table-manners |
| `lattenzaun` | mind-the-gap |

## Install a skill

Copy one folder unchanged to `~/.claude/skills/<name>/`
(on Windows `%USERPROFILE%\.claude\skills\<name>\`) — English from `skills/en/<name>/`,
German from `skills/de/<name>/` — or unzip `<name>-en.zip` / `<name>.zip` from the website
there. Claude Code loads it on the next start.

## License

MIT, see [LICENSE](LICENSE). Copyright (c) 2026 Falzbein und Andy.

## The other seasons

- Season 2: **Don't Panic – The Skill Suite for Panicking Models**, project `02-panik`, https://panik.special.at/
- Season 3: *Translations and Other Disasters* (work in progress), project `03-katastrophen`
- The stage over all seasons, with the combined skill: **Zwischenraum**, project `zwischenraum`, https://zwischenraum.special.at/

---

**Deutsch:** Die erste Spielzeit des Kabaretts von Falzbein und Andy: sechs kurze, optionale
Spickzettel für Claude Code gegen die immer gleichen Windows-Fallen. Einen Ordner aus
`skills/de/` (oder `skills/en/`) unverändert nach `~/.claude/skills/<name>/` legen, fertig.
Das Programmheft steht in `doku/LIESMICH.md`, die Seite unter https://grauen.special.at/.
