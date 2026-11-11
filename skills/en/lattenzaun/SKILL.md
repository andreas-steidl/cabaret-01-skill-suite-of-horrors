---
name: lattenzaun
description: A cheat sheet for spaces in paths and quotation marks that get lost on the way when PowerShell calls a native program - above all sc.exe, msiexec, cmd /c, schtasks and everything under “C:\Program Files”. Read it before you create a service with sc.exe, before you pass a path with spaces to an .exe, when a service won't start with error 1053, when Windows suddenly looks for “C:\Program”, or when `sc` does nothing at all (in PowerShell it means Set-Content). Part of the Skill Suite of Horrors. Optional, not required.
---

# Lattenzaun

*Once there was a picket fence, with space between to look right through.*
*(Christian Morgenstern, “Der Lattenzaun”)*

*In the poem an architect sees the gaps, takes them out, and builds a big
house from them. Windows sees the space in “Program Files” and thinks
exactly like that architect: look, there's room. And out of the gap it
builds something other than what you meant.*

## The three traps that snap shut together

1. **In PowerShell, `sc` is not sc.exe**, but `Set-Content`. `sc create …`
   silently writes a file called `create`. Always spell out **`sc.exe`**.
2. **Windows PowerShell 5.1 loses quotation marks** on the way to a
   native program. Inner `"` don't arrive unless they are escaped as `\"`,
   and sometimes not even then. PowerShell 7.3 and newer passes them through
   correctly (`$PSNativeCommandArgumentPassing`), but not for every kind of
   program, `cmd.exe` and `msiexec` stay stubborn.
3. **A path with spaces and no inner quotation marks** gets taken apart by
   the Service Control Manager: it looks for `C:\Program.exe` first, then
   `C:\Program Files\Python311\python.exe`. That is dangerous on top of it,
   because whoever drops a `C:\Program.exe` there gets started.

## What helps

- **Use the cmdlet instead of sc.exe**, then there is no native splitting:
  ```powershell
  New-Service -Name 'meindienst' -StartupType Automatic `
    -BinaryPathName '"C:\Program Files\Python311\python.exe" "D:\pfad\dienst.py"'
  ```
  Single quotes outside, double quotes inside: PowerShell leaves the inside
  alone.
- **If it has to be sc.exe:** after `binPath=` and `start=` comes a
  space, and there it is mandatory. And in Windows PowerShell 5.1, pass the
  rest through untouched with the stop-parsing token `--%`:
  ```powershell
  sc.exe --% create meindienst binPath= "\"C:\Program Files\Python311\python.exe\" \"D:\pfad\dienst.py\"" start= auto
  ```
- **python.exe is not a service.** A service program has to answer the
  Service Control Manager, otherwise after 30 seconds you get error 1053,
  “The service did not respond to the start or control request in a timely
  fashion” (on a German Windows: „Der Dienst antwortete nicht rechtzeitig
  auf die Start- oder Steuerungsanforderung“). Either write the script as a
  real service with `pywin32` (servicemanager), or put a service wrapper in
  front of it, or just use a scheduled task instead.
- **For everything else with spaces:** make the call in PowerShell with the
  call operator and separate arguments, `& "C:\Program Files\x\y.exe" $arg1 $arg2`,
  instead of building one finished string.

## The one check

After creating it, look at what is **really** registered:
```powershell
sc.exe qc meindienst          # line BINARY_PATH_NAME
(Get-CimInstance Win32_Service -Filter "Name='meindienst'").PathName
```
The quotation marks around `"C:\Program Files\…\python.exe"` have to be
there. If they are missing, the picket fence has won, no matter what the
command line reported. And first a trial run, then the real service:
Richtscheit found exactly this trap that way, before anyone walked into it.

*Written by Falzbein, November 3, 2026, after a find by Richtscheit.
Siblings in the Skill Suite of Horrors: `slash-n-back`,
`return-to-sender`, `fluchthelfer`, `tischlein-deck-dich`.*
