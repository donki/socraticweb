# sOC ScreenShare
- slug: screenshare
- plataformas: Windows 10 (version 2004) or later and Windows 11, 64-bit
- lema: Record a screen, all screens or a window with its sound into a light MP4, ready to share.
- github: https://github.com/donki/ScreenShare
- tiendas:
  - Microsoft Store: coming soon.
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/ScreenShare/releases (última: v2026.10.13.0; one self-contained executable)

## Description

sOC ScreenShare records what happens on your screen into an MP4 video you can send as it is: by default it comes out light (up to 1080p, about 30 MB per minute) and plays on any phone, browser or video player. You choose what to record —one screen, all of them together or a single window—, which sound goes in and which folder it is saved to, and press record.

When you record a window, only its sound is recorded: that application's, not the notifications or the music playing elsewhere on the PC. When you record a screen you can take everything that plays through a given set of speakers or headphones, or a single application, and add the microphone if you want to talk over it. Each source has its own volume.

It can start by itself: tell it which application —and, if you like, which window of that application, by its title— and as soon as it opens it is recorded with its sound, and saved when it closes. Two keyboard shortcuts start and stop recording without looking for the window. When it is done, play it, show it in its folder or copy the file to paste it into a chat or an email. It is free software, with no account, no ads and no trackers, and it connects to nothing.

## Main features

- Record one screen, all screens as they are arranged, or a window; if the window is resized, the video is not distorted.
- Sound of the recorded window, and only its own (including its helper processes, as browsers use).
- Sound of an output device or of a single application when recording a screen, plus the microphone, each with its own volume and level meter.
- H.264 or H.265 MP4 with AAC audio, using the graphics card encoder when there is one.
- «Best for sharing», «High» or custom quality: resolution, frames per second, bit rate, codec and audio, with the MB per minute shown before recording.
- Global keyboard shortcuts to start and stop (Ctrl+Shift+F9 and Ctrl+Shift+F10, configurable), even with the window hidden.
- Automatic recording when an application, or a given window of it, opens, stopping when it closes.
- Icon next to the clock with a red dot while recording; pause and resume.
- When done: play, open the folder or copy the file.
- Command line to record from scripts.

## User guide (support)

### Installation

1. Download the latest version from the GitHub releases page (https://github.com/donki/ScreenShare/releases): `sOCScreenShare.exe`.
2. Double-click it. There is nothing to install. If Windows warns that the publisher is unknown, click «More info» and «Run anyway».

Requirements: Windows 10 (version 2004) or later, or Windows 11, 64-bit. Recording only one application's sound needs Windows 11 or Windows 10 build 20348 or later; on older versions the app says so and does not record any other sound instead.

### First run

The first time, the «Setup guide» opens, with four steps (Back / Next at the bottom): where the videos go, the computer's sound (with a button to the Windows sound settings), the microphone (with a button to its Windows privacy settings) and the shortcuts and automatic recording (with Start with Windows). Open it again whenever you like with the help button (?).

### Main window

- **What to record**: One screen (click the one you want in the drawing of your screens), All screens or One window (from the list of open windows; a minimised one has to be restored to record it).
- **Sound**: with a screen, Computer sound (None, Everything playing through a device —choose which— or Only one application); with a window, Window sound (only its own). Microphone, with its device. Each with its volume bar.
- **Save**: the videos folder (Videos\ScreenShare by default), with buttons to choose it and open it; quality (Best for sharing, High or Custom) with the «Quality» button next to it, and the estimated size in MB per minute.
- **Bottom**: Record, Pause / Resume and Stop, with their shortcut underneath, and the recorded time.
- **Top right**: Guide, What's new, Español / English and About.
- **Last recording**: when done it appears at the top, with its size and length, and the Play, Show in folder and Copy file buttons.

### Quality

The «Quality» button opens a separate dialog. Video: maximum resolution (original, 2160p, 1440p, 1080p, 720p or 480p; it never upscales), frames per second (15, 24, 30 or 60), automatic bit rate or in Mbit/s, H.264 codec (plays everywhere) or H.265 (half the size, if your PC has an encoder) and rate control (variable, constant or constant quality). Audio: 96, 128, 160 or 192 kbit/s, 44.1 or 48 kHz, mono or stereo. At the bottom you see how the video will come out and how many MB it takes per minute.

### Automatic recording

In the settings, «Automatic recording»: add a rule with the application (from the open ones or by choosing its .exe) and, if you like, a window title (contains or regular expression) to record only a given screen of that application, such as a meeting window. Each rule has Active and Stop and save when the window closes. With automatic recording on, closing the window leaves ScreenShare next to the clock, and it can start with Windows. If a recording is already running it does not start another. A notification next to the clock shows when it starts and ends.

### Shortcuts

Ctrl+Shift+F9 starts recording and Ctrl+Shift+F10 stops. Change them in the settings by pressing the new combination; the ones Windows uses are not accepted, and it warns you if another application already has the same one.

## Frequently asked questions

**I record a window and there is no sound.**
Only that application's sound goes in: if it was not playing anything, the video has no sound. If your Windows is older than build 20348, the window tells you: there one application's sound cannot be separated.

**Why is my window not in the list?**
Only visible windows with a title are listed. If it is minimised, restore it; the refresh button updates the list.

**The video is too big.**
Use «Best for sharing», lower the resolution or the frames per second, or choose H.265 if your PC has it. The Quality dialog shows the MB per minute before recording.

**Does the ScreenShare window show up in the video?**
No: while recording, its windows are left out of the recording.

**Can I use it from a script?**
Yes: `sOCScreenShare.exe --record <seconds>` with options for what to record, the sound and the quality; `--help` lists them.

## Privacy

Everything stays on your PC: the videos in the folder you choose and the settings in your profile. The app sees the image and the sound only while recording; automatic recording looks at which windows open (program name and title) to compare them with your rules and stores none of it. It connects to nothing. No account, no ads, no trackers, no analytics.
