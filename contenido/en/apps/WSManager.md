# sOC WSManager
- slug: wsmanager
- publicar: no (2026-10-01: private repository until Josep decides; the page is ready)
- plataformas: Windows 10 (version 2004) or later and Windows 11, 64-bit
- lema: Any program as a Windows service: it starts it with the PC, watches it and brings it back if it crashes.
- github: https://github.com/donki/WSManager
- tiendas:
  - Microsoft Store: no aplica (services cannot be created from a Store package).
  - Google Play: no aplica (solo Windows).
- descarga_alternativa: https://github.com/donki/WSManager/releases (última: v2026.10.1.0; two self-contained executables)

## Description

sOC WSManager turns any program —a server, a script with its interpreter, a console tool— into a real Windows service: it starts with the PC even if nobody has signed in, runs with the account you choose and, if it crashes, comes back by itself. If it crashes again and again right after starting, it waits a little longer each time so as not to burn the processor.

From the icon next to the clock you see all your services with a coloured dot for their state, and you start, stop, pause, restart, edit or remove them without opening anything else. If one stops without being asked to, it tells you. The main window also shows the service process and the application process, and how many times it has restarted.

Each service is set up in a tabbed editor: the program and its arguments, the account, dependencies, priority and processors, how to stop it gently, what to do depending on how it exits, which files its output goes to (with the time on each line and rotation by size or age), its environment and commands that run at each moment. If you already have services made with another service manager, it imports them keeping their settings, by hand or automatically, and it can be undone. For scripts there is a full command line. It is free software, with no account, no ads and no trackers, and it connects to nothing.

## Main features

- Any program as a Windows service, with automatic, delayed, manual or disabled startup.
- Watching: if the application exits it starts it again, waiting longer (from 2 to 256 seconds) if it crashes in a loop; pausing the service cancels the wait.
- What to do on exit by exit code: start it again, do nothing, stop the service or let the Windows recovery actions apply.
- Staged stop: Ctrl+C, close its windows, ask its threads to quit and, if needed, end the process, also the ones it started.
- Output and errors to file, with the time on each line and rotation at start, while running or on demand.
- Service account: Local System, Local Service, Network Service or an account with a password (which goes straight to Windows).
- Icon in the notification area with every service, its state and its actions, and warnings if one stops.
- Import, by hand or automatic, of the services made with another service manager, with undo.
- Starts, stops, crashes and restarts logged in the Windows Event Viewer.
- Command line for scripts (create, change any option, start, stop, dump the configuration…).

## User guide (support)

### Installation

1. Download the latest version from the GitHub releases page (https://github.com/donki/WSManager/releases): `sOCWSManager.exe` (the app) and `sOCServiceHost.exe` (the service component). Put them in the same folder.
2. Open `sOCWSManager.exe`. Nothing else to install. If Windows warns that the publisher is unknown, click "More info" and "Run anyway".

Requirements: 64-bit Windows 10 (version 2004) or later, or Windows 11. Creating and changing services needs an administrator account (Windows asks for permission on each change).

### First run

The first time the "Setup guide" opens, with four steps (Back / Next at the bottom):

1. **Install the service component**: copies `sOCServiceHost.exe` to Program Files, where only administrators can change it and Windows can always read it. It is done by itself when you create the first service.
2. **Start with Windows** (optional): keeps WSManager next to the clock to see your services and get warnings.
3. **Create your first service**: "New service" button.
4. **Bring your services from another service manager** (optional): "Import" button.

The guide opens again whenever you want with the help button (?).

### Main window

**Left buttons** (icons only; the name shows on hover): New service (+), Edit, Start or continue, Pause, Stop, Restart, Rotate the output files now, Open the output (stdout / stderr) and Remove the service (in red, with confirmation).

**Right buttons**: Import from another service manager, Run as administrator (shield: a separate window where changes do not ask for permission one by one), Start with Windows, Setup guide, What's new, Español / English and About.

**List**: State (with its dot: green running, grey stopped, amber paused or waiting to restart), Service (display name and name), Startup, Account, Service PID, App PID and Restarts. Double-click or Enter edit; Delete removes. At the bottom, the result of the last action.

### Notification area icon

A click opens the window. Right-click shows one entry per service, with its state, and inside: Start, Stop, Pause or Continue, Restart, Edit, Open the output (stdout), Open the errors (stderr) and Remove the service. Below: New service, Import, Open the window and Exit. On hover it says how many services there are and how many are running. If a service stops without being asked to, an "A service stopped" notification shows.

### Service editor

At the top, the **Service name** (only when creating it). At the bottom, Cancel and Save; anything that is not valid is shown in red and not saved. If the service is running, the changes apply when you restart it.

- **Application**: Path of the program, Startup directory (empty: the program's folder) and Arguments. Paths can use variables such as %ProgramFiles%.
- **Details**: Display name, Description and Startup type (Automatic, Automatic (delayed), Manual, Disabled).
- **Log on**: Local System (with "Allow the service to interact with the desktop"), Local Service, Network Service or This account (Account, Password and Confirm the password, with the eye to show it). Without the administrator window, the password is asked for in the permission window when saving. The account gets the right to log on as a service.
- **Dependencies**: Services it depends on and Service groups it depends on, one per line.
- **Process**: Priority (from Realtime to Idle), Processors (All processors, or a list like 0-1,3) and No console window for the application.
- **Shutdown**: Send Ctrl+C, Close its windows (WM_CLOSE), Ask its threads to quit (WM_QUIT) and End the process, each with its wait in milliseconds (1500 by default); and Also stop the processes it started.
- **Exit actions**: Minimum run time before a restart counts as normal (1500 ms), When the application exits (Restart the application, Do nothing, Stop the service, End without stopping), Wait before restarting, and a By exit code list (add and remove).
- **I/O**: Input (stdin), Output (stdout) and Errors (stderr), with what to do if the file exists (Append to the end, Replace it…), and Put the date and time on each line.
- **File rotation**: Rotate the files when the service starts; While it runs (Do not rotate, Rotate when they reach the limits, Rotate at the limits and on demand); Older than (seconds) and Bigger than (bytes).
- **Environment**: Add or change variables, and Replace the whole environment (NAME=value, one per line; %VARIABLE% is expanded).
- **Hooks**: a command for each moment (before starting the application —exit code 99 cancels the start—, after starting it, before stopping it, after it exits, before and after rotating, when the power status changes and when the PC resumes).

### Import services

"Import from another service manager" button. The window has three parts:

- **Services of another service manager**: the ones found, ticked; "Import the selected ones" asks for confirmation and moves them to WSManager keeping all their settings. Running ones are stopped and started again.
- **Already imported**: each with "Undo the import", while the other manager's program is still on the PC.
- **Automatic import**: "Import services of another service manager automatically" (asks for administrator permission once) and "Restart right away the ones that are running" (if not, WSManager takes over at their next start). It creates a scheduled task that runs when the PC starts and every 15 minutes; each import shows a notification.

### About

Version, What's new, Report an issue or an idea, Language (Español / English, with their flags), Privacy, License and Legal notice.

## FAQ

**Why does it ask for administrator permission on each change?**
Creating, changing, starting or stopping services is for administrators in Windows. The app runs without privileges and asks only for each operation, without leaving anything privileged running. If you are going to make many changes in a row, use the shield button ("Run as administrator").

**My program crashes right after starting and the service says "Waiting to restart".**
That is the growing wait: each crash in a row doubles the wait, up to 256 seconds. Look at the output (output button) and at the Event Viewer (source sOCWSManager) to see why it exits. Pause the service to cancel the pending restart.

**Where do I see what my program writes?**
Set a file in the I/O tab (Output and Errors can be the same). Then "Open the output" opens it with the Windows program.

**I imported a running service with automatic import and nothing changed.**
By default, running ones move to WSManager at their next start (for example when the PC restarts), which is the lowest-risk moment. If you prefer them restarted right away, tick "Restart right away the ones that are running".

**Does it store the account passwords?**
No: they go straight to Windows, which keeps them for the service.

## Privacy

Everything stays on your PC: the services are stored by Windows, and the app only keeps its language and window size in your user profile. It connects to nothing. No account, no ads, no trackers, no analytics. Account passwords go straight to Windows and are never stored by the app.
