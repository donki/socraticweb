# sOC Remote Connections Manager
- slug: rcmanager
- plataformas: Windows 10 (version 2004) or later and Windows 11, 64-bit
- lema: Your remote desktops, SSH terminals and file servers, in tabs and in a single window.
- github: https://github.com/donki/RCManager
- tiendas:
  - Microsoft Store (publicada): https://apps.microsoft.com/detail/9MXKDZMLCS99 (enlace de Josep, 2026-09-25; ficha pública comprobada)
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/RCManager/releases (última: v2026.9.23.1; ejecutable autocontenido y paquete MSIX)

## Description

sOC Remote Connections Manager brings together in a single window all the connections you use to work with servers: Windows Remote Desktop (RDP), SSH terminal, and file transfer over SFTP, SCP, FTP and FTPS. On the left you have a tree with your connections organized in folders, plus a search box; on the right, each session opens in its own tab, so you can have several servers open at once and jump from one to another.

Remote Desktop uses the same client that comes with Windows, with all its familiar options (display, local resources, experience, certificate, gateway…), and the remote desktop automatically fits the size of the tab. For files you get a two-pane explorer, your PC on one side and the server on the other, where you upload and download entire folders by dragging, and you can even edit text files on the server without downloading them.

Your connections are stored on your PC with the passwords encrypted for your Windows user or, if you prefer, in your own Google Drive or OneDrive, encrypted with a passphrase only you know, so you have the same connections on all your computers. You can import what you already have in Remote Desktop Manager or in .rdp files. It is free software, with no account, no ads and no trackers.

## Main features

- RDP, SSH, SFTP/SCP and FTP/FTPS connections, each session in its own tab.
- Connection tree with nested folders, search, drag and drop, and it stays exactly as you left it.
- Remote Desktop with all the options of the Windows client, organized in the same tabs as the original, a resolution that follows the tab, full screen on the monitor of your choice, and use of all your monitors.
- Your PC's drives inside the remote desktop, and a shared clipboard with text, images and files.
- SSH terminal with colors, scrollback, copy and paste, and sign-in with a password or a private key.
- Two-pane file explorer with a transfer queue, progress and cancel, and changing permissions and owner on Linux servers.
- Built-in text editor that saves directly to the server.
- Per-tab zoom (terminal and pane font size, remote desktop scale), remembered per connection.
- Connections on this PC or synced, encrypted, in Google Drive or OneDrive.
- Import from Remote Desktop Manager (.rdm) and from .rdp files.

## User guide (support)

### Installation

1. Download the latest version from the GitHub releases page (https://github.com/donki/RCManager/releases). There are two options:
   - The `sOCRCManager.exe` executable: no installation needed, just double-click it.
   - The `.msix` package: installs like any other Windows app.
2. You can also install it from the [Microsoft Store](https://apps.microsoft.com/detail/9MXKDZMLCS99), which keeps it up to date for you.

Requirements: Windows 10 (version 2004) or later, or Windows 11. Remote Desktop uses the client already built into Windows; there is nothing else to install.

### Getting started

1. Open the app. The tree is empty and tells you: "No connections yet. Add one with + and it will show up here."
2. If you already have connections in Remote Desktop Manager or in .rdp files, go to Settings (gear icon) › Import connections. Otherwise, click "New connection" (+).
3. Fill in at least the Name and the Host, choose the Type and click Save.
4. Optional: in Settings, choose whether to store your connections only on this PC or in Google Drive / OneDrive.

You don't need to create any account. Only if you choose to store your connections in the cloud will you sign in with your Google or Microsoft account.

### Everyday use

- To connect: double-click the connection, or select it and click Connect (or press Enter), or drag it to the tab area.
- If the connection has no saved password, you are asked for it when connecting, with the "Remember it on this PC (encrypted)" checkbox.
- Each session opens in a tab. Switch between them with a click, with Ctrl+Tab / Ctrl+Shift+Tab, or with the open sessions button on the bottom bar.
- To edit a connection: select it and click Edit, or Ctrl + double-click.
- To close a session: "Disconnect this tab" button on the tab itself.

### Main window

**Tree toolbar (from left to right)**
- Connect: opens the selected connection.
- New connection (+): opens an empty connection editor.
- New folder: asks for the "Folder name" and creates it.
- Edit: opens the editor for the selected connection (or renames the selected folder).
- Duplicate: creates a copy of the selected connection.
- Delete: asks for confirmation ("Delete "…"?"). If it is a folder, it also deletes the connections inside it ("Delete folder "…" and the N connections inside?").
- Search…: filters the tree by name, host, user, folder or notes; only folders that contain a matching connection are shown.

**Connection tree**
- Double-click: connect. Ctrl + double-click: edit. Enter: connect. Del: delete.
- Dragging a connection or a folder onto another folder moves it there (onto a connection, into that connection's folder). The target folder is highlighted as you drag over it.
- Dragging a connection to the tab area opens it.
- When you close the app, it remembers the expanded folders, the selected connection and the width of the pane.

**Buttons at the bottom of the tree**
- Settings (gear): "Settings: where connections are stored", import and window behavior.
- Open the connections file folder: opens the folder where your connections are stored in File Explorer.
- Español / English: switches the language instantly.
- About: contact the author, language, privacy, license and legal notice.

**Tab area**
- With no open sessions it shows: "Double-click a connection, or select it and press Connect. Each session opens in its own tab."
- Each tab has its own buttons:
  - Smaller / Bigger (− and +): zoom for the tab. In SSH it changes the terminal font size; in file sessions, the font size of the panes; in RDP, the scale of the remote desktop (from 100 to 200%). It is remembered the next time you open that connection.
  - Full screen (F11; Ctrl+Esc to come back).
  - Disconnect this tab.

**Status bar**
- Open sessions: a menu with all the tabs to switch to any of them, handy when the remote desktop grabs the keyboard (shortcuts Ctrl+Tab / Ctrl+Shift+Tab).
- Status messages: "Connecting to…", "Connected to…", the result of the cloud sync, and so on.

**Full screen**
- RDP: uses the full screen mode of the Windows client itself, with its connection bar at the top (it hides automatically; its minimize and close buttons work: close disconnects and closes the tab).
- SSH and files: the window fills the whole screen and a bar appears at the top that hides automatically and comes back when you move the mouse to the top edge, with the session name, "Leave full screen (Ctrl+Esc)", open sessions and "Disconnect this tab".
- The screen it opens on is chosen in the connection editor, with the "Full screen on" option.

**Notification area**
- When you minimize, the window hides and leaves its icon next to the clock (if you don't see it, it is among the hidden icons in Windows 11). One click brings it back; right-click for "Open" and "Exit". Open sessions stay alive. You can turn this off in Settings › Window.

### Connection editor

It opens with "New connection" or "Edit". The tabs shown depend on the type: RDP shows General, Display, Local resources, Experience and Advanced; SFTP / SCP and FTP / FTPS show General and Transfers; SSH only General. At the bottom, Cancel and Save ("The name and the host are required.").

#### General tab (all types)
- Name: how it appears in the tree.
- Type: RDP, SSH, SFTP / SCP or FTP / FTPS. When you change it, the usual port is suggested (3389 for RDP, 22 for SSH and SFTP, 21 for FTP and 990 for implicit FTPS).
- Folder: the tree folder the connection goes in (you can pick one or type a new one).
- Host: name or IP address.
- Port.
- User.
- Domain (RDP only).
- Password, with an eye button to show or hide it. "Leave empty to be asked when connecting."
- Private key (file) (SSH and SFTP), with a "Choose file" button: "OpenSSH or PEM file. If set, the password is the key passphrase."
- Encryption (FTP / FTPS only): "None (plain FTP)", "FTPS explicit (AUTH TLS, port 21)" or "FTPS implicit (port 990)".
- "Transfer with SCP instead of SFTP (browsing always uses SFTP)" (SFTP / SCP only).
- Remote folder to open and Local folder to open (SFTP and FTP): "Leave empty for the server's default folder and your user profile." If you don't set a remote folder, it starts at the root of the server (/).
- Full screen on: "The screen the window is on" or a specific screen ("Screen N (width×height)", marking the primary one).
- Notes: free text (the search box finds it too).

#### Display tab (RDP)
- Remote desktop size:
  - "Fit the tab (follows the window)" (default): asks the server for the resolution that fits the tab, crisp and with no bars, and changes it when you resize the window.
  - Fixed sizes: 1024 × 768, 1280 × 800, 1366 × 768, 1600 × 900, 1920 × 1080, 1920 × 1200, 2560 × 1440.
  - "Custom…": enables Width and Height (at least 200 pixels each). A fixed size is scaled to the tab.
- "Use all my monitors in full screen": in full screen the remote desktop gets one monitor for each screen on your PC (the session reconnects in full screen to get them); in the tab it is always a single screen. Off by default.
- Colours: "High colour (15 bit)", "High colour (16 bit)", "True colour (24 bit)" or "Highest quality (32 bit)" (default).
- "Show the connection bar in full screen" (on by default).

#### Local resources tab (RDP)
- Remote audio playback: "Play on this PC" (default), "Play on the remote computer" or "Do not play".
- "Record from this PC (microphone)": uses your microphone in the remote session (off by default).
- Windows key combinations (Alt+Tab, Win…): "On this PC", "On the remote computer" or "On the remote computer only in full screen" (default).
- Local devices and resources to use in the remote session:
  - Printers (on by default).
  - Clipboard (text, images and files) (on by default).
  - Drives of this PC (copy and move files with Explorer) (on by default): your drives appear on the remote computer as "C on your PC" under This PC, including USB drives you plug in during the session.
  - Smart cards and Windows Hello (on by default).
  - Serial ports (off by default).
  - Other Plug and Play devices (cameras, players…) (off by default).

#### Experience tab (RDP)
- Visual effects (turn off on slow links), all on by default:
  - Desktop background.
  - Font smoothing.
  - Desktop composition.
  - Show window contents while dragging.
  - Menu and window animation.
  - Visual styles.
  - Persistent bitmap caching.
- Connection: "Reconnect if the connection is dropped" (on by default).

#### Advanced tab (RDP)
- If server authentication fails (certificate): "Connect and don't warn me", "Warn me" (default; it warns you and lets you continue, like the Windows client) or "Do not connect".
- "Administration session (console, /admin)".
- Remote Desktop Gateway: "Do not use a gateway" (default), "Always use the gateway" or "Use the gateway except for local addresses".
  - Gateway server.
  - "Use the same user and password as the remote desktop" (on by default). If you untick it, separate User, Domain and Password fields for the gateway appear.

#### Transfers tab (SFTP / SCP and FTP / FTPS)
- Files at a time: from 1 to 8 (default 2). "Each simultaneous transfer opens its own connection to the server. 1 is the safest; 2–4 speeds up many small files."
- Retries on failure: from 0 to 5 (default 1).
- If the file already exists at the destination: "Ask before overwriting" (default), "Overwrite" or "Skip".
- "Keep the original modification date" (on by default).
- "Show hidden files (dotfiles) when opening".
- Keep-alive (seconds, 0 = off): default 30.
- Timeout (seconds): default 20.
- FTP only:
  - Data connections: "Passive (the usual choice behind a router)" (default) or "Active".
  - File name encoding: UTF-8 (default) or Latin-1 (ISO-8859-1).

### Remote Desktop session (RDP)

- The desktop appears inside the tab and fits its size if you chose "Fit the tab".
- Zoom (− and +) changes the scale of the remote desktop between 100 and 200%, and is restored when you open the connection again.
- To copy files between your PC and the server: Ctrl+C in one File Explorer and Ctrl+V in the other, or use your PC's drives that appear on the remote computer.

### SSH session

- Terminal with colors, cursor, and full-screen programs such as vim, htop or less.
- Scrollback: mouse wheel or Shift+Page Up / Shift+Page Down.
- Copy: Ctrl+Shift+C. Paste: Ctrl+Shift+V. Right-click: copies if there is selected text, and pastes if there isn't.
- The terminal adapts to the size of the window.

### File session (SFTP / SCP and FTP / FTPS)

While connecting, the tab shows "Connecting to…"; once connected, the two-pane explorer appears: this PC on the left and the server on the right. Each pane has its own path bar (you can type a path directly) and Name, Size and Modified columns (and, on Linux/Unix servers, Permissions and Owner).

Pane buttons:
- This PC (local pane): to change drives.
- Up one level (Backspace).
- Refresh.
- New folder (F7).
- Rename (F2).
- Delete (Del): "Folders go with everything inside; there is no recycle bin."
- Upload the selection to the server / Download the selection to this PC (F5, or drag it to the other side).
- Open: locally, with the Windows default program; remotely, a copy with the default program.
- Edit here (text files).
- Copy the path.
- Show hidden files.
- Permissions and owner (Unix servers).
- Cancel the transfer (while one is in progress).

Double-clicking a text file on the server opens it in the built-in editor; on a local file, it opens it with its Windows program. Transfers are queued, with progress ("Uploading… · N of M").

If a file already exists and the connection is set to "Ask before overwriting", a "File already exists" dialog appears with Overwrite, Skip and the "Do the same for the rest" checkbox.

**Permissions and owner window** (Linux/Unix servers only)
- Permissions: Read, Write and Execute checkboxes for Owner, Group and Others, with the Octal value shown.
- Owner and group: names or numbers; empty = no change. With SFTP, changing by name runs a command over SSH with the same credentials; most FTP servers do not allow changing the owner.
- "Apply to everything inside the folders".
- Apply.

**Built-in text editor**
- Save to the server (Ctrl+S), keeping the same encoding and line endings.
- Find (Ctrl+F): Next (Enter) and Previous (Shift+Enter).
- Ctrl + and Ctrl − change the font size (it is remembered).
- The bottom bar shows the line and column, and the time of the last save.
- If you close it with unsaved changes, it asks whether to save them to the server (Save, Discard or Cancel).

### Settings

**Where connections are stored**
- This PC: connections stay in your user profile; nothing leaves the computer.
- Google Drive: you sign in with Google in the browser; the file goes to the app's private folder in your Drive, with no access to your other files. On Google's permissions screen you must tick the Google Drive checkbox.
- OneDrive: you sign in with Microsoft; the file goes to the app folder in your OneDrive, with no access to your other files.
- Below, it shows which account you are signed in with and the last sync.

**Encryption passphrase** (only with Google Drive or OneDrive)
- Passphrase box, with an eye button to show it. At least 8 characters.
- Save the passphrase and sync.
- Sync now.
- The passphrase never leaves your PC and is not stored in your account: use the same one on every computer. If you forget it, the cloud copy cannot be read. Without a passphrase nothing is uploaded.
- At startup the cloud copy is downloaded if it is newer, and every change is uploaded; if you save from two computers, the last one wins.

**Import connections**
- "Import from Remote Desktop Manager (.rdm) or Remote Desktop files (.rdp)" button.
- From an .rdm file, RDP, SSH, FTP/FTPS and SFTP/SCP connections are imported with their folders. From .rdp files (you can select several at once) you get one connection per file, with its name and options.
- Passwords are not imported: they are asked for when connecting. When it finishes, it tells you how many were imported, how many already existed and how many were skipped because they are of unsupported types.

**Window**
- "Minimize to the notification area" (on by default). When off, the window minimizes to the taskbar like any other window.

Close: closes Settings.

### About

Contact ("Write to the author"), language switch, privacy, MIT license and legal notice.

### Shortcut options

You can create a shortcut that opens a connection at startup: `sOCRCManager.exe --open "Connection name"`. Also, `--edit "Name"` opens its editor, and `--edit-file "Name" "/path"` opens a file on the server in the built-in editor.

## FAQ

**It won't connect to an SSH, SFTP or FTP server. What's wrong?**
A "Could not connect" window appears with the reason: the name does not resolve (check the host name or the DNS), the port is closed (wrong port or the service is stopped), it does not answer in time (the machine is off or a firewall is blocking it), there is no route (check the network or the VPN), wrong user name or password, or the server does not offer TLS. In that last case, try plain FTP or "FTPS implicit" on port 990.

**Remote Desktop says it cannot continue because of the certificate.**
In the connection editor, Advanced tab, "If server authentication fails" must be set to "Warn me" (it lets you continue after warning you) or "Connect and don't warn me". "Do not connect" blocks servers with a self-signed certificate.

**When I open an RDP connection the zoom goes back to 100%.**
Since version 2026.9.23.1 the zoom is applied after signing in and is retried for a few seconds until the server accepts it. Update to the latest version.

**I minimized the window and it disappeared.**
It is in the notification area, next to the clock (in Windows 11, it may be among the hidden icons, under the ^ arrow). One click brings it back. If you would rather have it minimize to the taskbar, turn off Settings › Window › "Minimize to the notification area".

**With "Use all my monitors", why does the tab only have one screen?**
Inside the tab the remote desktop always uses a single screen. When you go full screen the session reconnects (a couple of seconds) with one remote monitor for each screen on your PC, and when you go back to the tab it returns to one.

**I signed in with Google and sync fails.**
Google shows each permission as a checkbox; if the Google Drive one is left unticked, the app warns you: "sign in again and tick the Google Drive box on Google's permissions page". Sign in again from Settings and tick it.

**On another PC it says "The cloud file was encrypted with a different passphrase."**
In Settings › Encryption passphrase you have to type exactly the same passphrase you used on the first computer. If you have forgotten it, the cloud copy cannot be recovered.

**I imported from Remote Desktop Manager and it asks me for the passwords.**
That is expected: passwords in RDM and in .rdp files are encrypted for the user who saved them and cannot be imported. You are asked for them when connecting, and you can tick "Remember it on this PC (encrypted)".

## Privacy

Connections are stored in your Windows user profile with the passwords encrypted for your account, and sessions go straight from your PC to your servers. Only if you choose Google Drive or OneDrive is the connections file uploaded to the app's private folder in your own account, encrypted with a passphrase that never leaves your PC. There is no server of our own, no account, no ads, no trackers and no analytics.
