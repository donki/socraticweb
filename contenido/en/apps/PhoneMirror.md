# sOC Phone Mirror
- slug: phonemirror
- plataformas: Windows 10 (version 2004) or later and Windows 11, 64-bit; controls Android 5.0 or later phones and tablets
- lema: Your Android phone's screen on Windows, controlled with your mouse and keyboard.
- github: https://github.com/donki/PhoneMirror
- tiendas:
  - Microsoft Store (en revisión): https://apps.microsoft.com/detail/9N0S24Z4DLS1 — identificador de producto 9N0S24Z4DLS1 (fuente: nota del proyecto sobre el rechazo del 2026-09-15). Rechazada el 2026-09-15 y reenviada el 2026-09-22 a la espera de certificación (fuente: D:\sOCProjects\TAREAS.md, «Josep lo reenvió a la Store el 2026-09-22 (queda esperar la certificación)»). Comprobado el 2026-09-25: el catálogo público de la Store todavía responde «producto no encontrado» para ese identificador, así que el enlace aún no funciona. El README.md del repositorio enlaza de momento a la búsqueda por nombre.
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/PhoneMirror/releases (última: v2026.9.21.0; ejecutable y paquete MSIX)

## Description

sOC Phone Mirror shows your Android phone's or tablet's screen in a Windows window and lets you control it from your PC: tap with the mouse, type with the computer's keyboard, copy and paste between the two, and drag files over to send them to the phone. It's really handy for replying to messages with a real keyboard, giving demos, recording tutorials or simply not having to pick up your phone while you work.

Plug your phone in by USB and it connects on its own. The window adapts to the phone: if you open a game or a video in landscape, the window turns landscape along with it. If you have several phones, you can open a window for each one, and you can also connect over Wi-Fi with no cable.

Everything goes through the cable (or your local network) between the PC and the phone: there's no account, no server, and nothing goes out to the internet. Everything needed to talk to the phone is already included in the app, so you don't have to install anything else. It's free software, with no ads or trackers.

## Main features

- Your phone's screen in real time in a Windows window that adapts to portrait and landscape.
- Tap, swipe and scroll with the mouse; right button for back and middle button for home.
- Type with your PC's keyboard, using your keyboard layout.
- Shared clipboard both ways (Ctrl+C / Ctrl+V and buttons).
- Back, home, recent apps, notifications, screen on/off, rotate, volume and mute buttons.
- Screenshot of the phone's screen with one click.
- Drag an APK to install it, or any file to copy it to the phone's Download folder.
- Wi-Fi connection, including pairing with a code on Android 11 or later.
- Lives in the system tray, can start with Windows and open on its own when you plug in a phone.
- One window per phone if you have several connected.

## User guide (support)

### Installation

1. Download the latest version from https://github.com/donki/PhoneMirror/releases. You can choose:
   - The `sOCPhoneMirror.exe` executable: that alone is all you need, no installation required.
   - The `.msix` package, which installs like any other Windows app.
2. Once it's published, you'll also be able to install it from the Microsoft Store.

The tool it uses to communicate with Android (adb) is already included: the first time you open the app, it sets it up on its own. With the standalone executable, it also becomes available to new Windows consoles ("adb added to your PATH…").

### Setting up your phone (just once)

1. On your phone, turn on Developer options (usually by tapping "Build number" seven times in Settings › About phone).
2. In Settings › Developer options, turn on **USB debugging**.
3. On **Xiaomi, Redmi and POCO**, also turn on **"USB debugging (Security settings)"**: without it the screen shows but the mouse and keyboard can't control it.
4. Plug your phone in by USB. The phone asks whether you trust this PC: accept on its screen.

### Getting started and everyday use

1. Open sOC Phone Mirror with your phone plugged in: it connects on its own and the phone's screen appears.
2. If it doesn't appear, the window tells you what's going on: "No phone connected…" or "The phone is asking whether to trust this computer. Accept on its screen."
3. Control your phone with the mouse and keyboard (see "Using the mouse and keyboard").
4. Closing or minimizing the window hides it in the system tray; to exit completely, use "Quit" in the icon's menu.

There's no need to create an account or sign in.

### Main window: top bar

From left to right:

**Connection**
- Phone selector: lists the detected phones (model and serial number).
- Look for phones again.
- Connect over Wi-Fi: opens the network connection window (see below).
- Connect: starts mirroring the selected phone.
- Disconnect: ends the session. After you disconnect manually, it won't reconnect to that phone on its own until you unplug it and plug it back in.

**Phone buttons**
- Back.
- Home.
- Recent apps.
- Notifications: pulls down the notification shade.
- Screen on / off.
- Rotate.
- Volume down and Volume up.
- Mute / unmute the phone (this is the phone's own sound; this window doesn't play audio).

**Tools**
- Save a screenshot: saves the phone's screen to the Pictures\Phone Mirror folder on your PC ("Screenshot saved to…").
- Copy the phone clipboard to the PC.
- Paste the PC clipboard on the phone.
- Keep on top: keeps the window above all others (toggle).
- Open when a phone is plugged in (starts with Windows, in the tray): toggle. When on, the app starts with Windows hidden in the tray and opens on its own when you plug in a phone ("The app will start with Windows and open when a phone is plugged in."). When off, it no longer starts with Windows.
- Español / English: changes the language right away.
- About.

### Center area

- With a session: the phone's screen, which adapts to the window.
- Without a session: a notice with what's missing and a reminder of how to turn on USB debugging.
- If for some reason adb can't be found, two buttons appear: "Download the Android platform-tools from Google (about 7 MB)" and "Find adb.exe on this PC…" (the path you choose is remembered).

### Bottom bar

- Connection status: "Connecting to…", the connected phone and its resolution, "Disconnected" or "The connection ended: …".
- Frames per second.

### Using the mouse and keyboard

| Gesture | What it does |
|---|---|
| Click and drag | Tap and swipe |
| Right button | Back (or turns the screen on if it's off) |
| Middle button | Home |
| Wheel / Shift+wheel | Scroll vertically / horizontally |
| Typing | Types on the phone (letters as text; arrows, Enter, Backspace, Delete, Esc, Tab, Home, End, Page Up, Page Down and media keys as keys) |
| Ctrl+V | Pastes the PC clipboard on the phone |
| Ctrl+C | Copies what's selected on the phone and brings it to the PC |
| Drag an .apk onto the window | Installs it on the phone |
| Drag any other file | Copies it to the phone's Download folder |

### Connect over Wi-Fi window

"The phone must have network debugging enabled, and be on the same network as this PC."

- Phone address (IP or IP:port), with a Connect button. Addresses that have worked are remembered (each with "Forget this address") and reconnect on their own at startup if the phone is on and on the same network.
- **First time on Android 11 or later**: on your phone, go to Developer options › Wireless debugging › Pair device with pairing code. The phone shows an address with its port and a six-digit code:
  - Pairing address (IP:port).
  - Pairing code.
  - Pair. Then connect above with the address shown under "Wireless debugging" (it's a different port).
- Another way: with the phone plugged in by cable once, run "adb tcpip 5555" and it will accept connections to its IP until it restarts.

### System tray

- The app lives in the tray: closing or minimizing the window hides it instead of exiting. The first time, a notice appears: "Still running here, in the tray: click to open, or Quit from the menu."
- Click the icon: opens the window. Right-click: Open and Quit.
- With no phone, the icon shows "sOC Phone Mirror · waiting for a phone".

### Multiple windows and multiple phones

- If you open the app when it's already open, it asks: "Show the selected window" (from a list showing each window's phone) or "New window". That way you can have one window for your phone and another for your tablet.
- Each window's title includes the connected phone.

### About

Contact ("Write to the author"), language, privacy, MIT license and legal notice.

## FAQ

**I can see my phone's screen but the mouse and keyboard don't do anything (Xiaomi, Redmi, POCO).**
On those brands, in addition to USB debugging, you have to turn on the "USB debugging (Security settings)" option in Developer options. Without it, the screen shows but can't be controlled.

**It says "No phone connected".**
Check that the cable carries data (not just charging), that USB debugging is turned on, and click "Look for phones again". Try another USB port if it still doesn't show up.

**It says "The phone is asking whether to trust this computer".**
Unlock your phone and accept the USB debugging prompt on its screen (you can check the option to always trust this computer).

**I closed the window and the app is still running.**
That's on purpose: it lives in the system tray so it can connect when you plug in your phone. To exit completely, right-click its icon (on Windows 11 it may be under the ^ arrow for hidden icons) and choose "Quit".

**It doesn't connect on its own when I plug in my phone.**
If you clicked Disconnect, it won't reconnect to that phone until you unplug it and plug it in again. To also have it open on its own when Windows starts, turn on the "Open when a phone is plugged in" button.

**I can't connect over Wi-Fi.**
Your phone and PC have to be on the same network. On Android 11 or later, first pair with the six-digit code and then connect with the address shown under "Wireless debugging", which uses a different port from the pairing one.

**I hear the sound on my phone, not on my PC.**
That's normal: the app doesn't stream audio. The volume and mute buttons control the phone's own sound.

**I dragged a file and I don't know where it went.**
APKs get installed; any other file is copied to the phone's Download folder. The bottom bar confirms "… copied to Download".

## Privacy

Everything happens between your PC and your phone over the USB cable (or over your local network if you use Wi-Fi): the screen is shown on the PC and your taps go straight to the phone. Nothing is stored except the screenshots you take (in Pictures\Phone Mirror) and the text you copy, and nothing goes out to the internet. No account, no ads, no trackers and no analytics.
