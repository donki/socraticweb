# sOC AutoTask
- slug: autotask
- plataformas: Windows 10 (version 2004) or later and Windows 11, 64-bit
- lema: Record what you do with the mouse and keyboard and let it repeat by itself.
- github: https://github.com/donki/AutoTask
- tiendas:
  - Microsoft Store: not yet (listing prepared, not submitted).
  - Google Play: not applicable (Windows only).
- descarga_alternativa: https://github.com/donki/AutoTask/releases (latest: v2026.10.01.0; self-contained executable and MSIX package)

## Description

sOC AutoTask is a macro recorder for Windows. Press Record, do once the task you're tired of repeating —filling in a form, arranging some windows, pressing the same buttons—, press Stop, and from then on AutoTask repeats it for you: just as you did it, faster, or in a loop until you stop it.

The window is a small bar that stays out of the way, and everything also works with two keyboard shortcuts from any program. If a playback gets out of hand, an emergency key stops it at once and releases every key. You can save your recordings, tweak them in an event editor and even turn them into a small .exe program that plays them on any PC with nothing to install.

It doesn't use the internet, has no account or ads, and is free software.

## Main features

- Records mouse moves and clicks (all five buttons), the wheel and the keyboard, in any program.
- Global shortcuts: Ctrl+Alt+Shift+R to record and Ctrl+Alt+Shift+P to play, configurable.
- Emergency stop with Pause, Scroll Lock or by holding Esc.
- Speed from 0.5× to 100× or your own; repeat once, N times or forever, with a pause between loops.
- Saves and opens recordings (.soctask), with recent files and drag and drop.
- Turns a recording into a standalone .exe.
- Event editor: delete, trim, simplify mouse moves, change or insert waits, undo.
- Multiple monitors and scaled displays.
- Always on top, next to the clock when minimized, light or dark, Spanish and English.

## User guide (support)

### Installation

1. Download the latest version from https://github.com/donki/AutoTask/releases: the `sOCAutoTask.exe` executable (no installation needed) or the `.msix` package.
2. Open `sOCAutoTask.exe`. If Windows warns that the publisher is unknown, click "More info" and "Run anyway".

Portable mode: put an empty file named `portable.ini` next to the exe and settings are stored in that same folder (for example, on a USB stick).

### Getting started

The first time, the **Setup guide** opens, step by step: global shortcuts, emergency stop, what gets recorded, opening recordings with a double-click, administrator programs and a quick try. Each step says whether it's done, pending or optional, and has a button that does it. Later it opens from **More › Setup guide**.

### Everyday use

1. Press **Record** (or Ctrl+Alt+Shift+R). The window shows "Recording" with the time and the events.
2. Do the task with the mouse and keyboard.
3. Press **Stop** (or Ctrl+Alt+Shift+R again). The shortcut isn't recorded.
4. Press **Play** (or Ctrl+Alt+Shift+P). To stop it early: the same shortcut, the button or the emergency stop.
5. **Save** to keep it as a `.soctask` file.

### Main window

- **Open**: a `.soctask` recording, a `.rec` file from other macro tools (experimental) or an exe made with AutoTask. You can also drop the file on the window.
- **Save**: in `.soctask` format.
- **Record / Stop** and **Play / Stop**.
- **Compile**: creates an `.exe` that plays the recording when opened.
- **Edit**: opens the event editor.
- **Settings**: speed, repeats, shortcuts, emergency stop, window, language and files.
- **More**: recent files, Save as, Import .rec, open the data folder, guide, what's new, restart as administrator, About and Exit.
- Below, the status (recording, playing with the time left, finished…) and the loaded recording: name, events, duration, speed and repeats. An asterisk means unsaved changes.

### Settings

- **Playback** (saved with the recording): speed (0.5×, 1×, 2×, 4×, 10×, 100× or custom from 0.1 to 1000), repeat once / this number of times / forever, pause between repeats (seconds) and countdown before starting (0 to 10 s).
- **Shortcuts and emergency stop**: click the box and press the combination (it needs Ctrl, Alt, Shift or Win plus another key). Emergency: Pause/Break, Scroll Lock and Esc held for the seconds you choose.
- **What is recorded**: the keyboard (turn it off to record only the mouse) and mouse moves.
- **Window**: always on top, text under the icons, minimize to the notification area, theme (same as Windows, light or dark) and language.
- **Files**: open `.soctask` files with AutoTask on double-click (only for your user).

### Event editor

A list with number, time, wait, type and detail of each event. Buttons: **Delete** (Del), trim **Start** and **End**, **Simplify** mouse moves (with a tolerance in pixels, or keeping only the last move before each click), **Wait** for the selected events, **Scale** the waits (percentage), **Insert** a wait and **Undo** (Ctrl+Z). Nothing changes until you press Apply.

### Compile to .exe

Choose a name and folder. The exe plays the recording with its speed, repeats and countdown, and stops with the same emergency keys. It needs neither AutoTask nor any installation.

## FAQ

**My antivirus blocked the exe I compiled.**
Some antivirus programs distrust new, unsigned programs that move the mouse and keyboard. The exe is safe: it doesn't use the internet, doesn't write to disk or install anything, and only repeats what you recorded. You can add it to your antivirus exceptions.

**It does nothing in a particular program.**
If that program runs as administrator, Windows doesn't let a normal program send it keys or clicks. AutoTask detects it and offers to restart as administrator (also in More › Restart as administrator). Some games don't accept simulated keys or clicks.

**The clicks land somewhere else.**
Playback repeats the exact screen positions: if windows have moved or you changed monitor or resolution, clicks land where things were when you recorded. Keep the windows as they were.

**Does it record my passwords?**
It records everything you type while recording, passwords included, and it stays in the file or the exe. Don't record passwords, or turn off "Record the keyboard" in Settings.

**The shortcut doesn't work.**
Another program may be using the same combination: AutoTask warns about it and the guide marks it as pending. Choose another one in Settings.

**How do I stop an endless playback?**
With the same play shortcut, the Stop button, or the emergency stop: Pause, Scroll Lock or holding Esc for a second.

## Privacy

sOC AutoTask doesn't use the network and collects no data. What you record stays on your PC and is only saved where you decide. Settings and an error log (with nothing of what you recorded) are stored in your user profile or next to the exe in portable mode. No account, no ads, no trackers, no analytics.
