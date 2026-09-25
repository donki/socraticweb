# sOC Uninstaller
- slug: uninstaller
- plataformas: Android / Windows
- lema: Check several apps and uninstall them all at once, on your phone and your PC.
- github: https://github.com/donki/Uninstaller
- tiendas:
  - Google Play (producción, con la versión 2026.08.01 y el nombre «Uninstaller»; la 2026.09.19.07 está en prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.uninstaller (ficha pública accesible el 2026-09-25; D:\sOCProjects\08-PENDIENTE-Uninstaller.md y D:\sOCProjects\01-TAREAS-Uninstaller.md: la alpha 2026091907 se publicó el 2026-09-24 y espera la revisión de Google antes de pasar a producción)
  - Microsoft Store (no publicada): sin ID todavía. El nombre «sOC Uninstaller» está por reservar en Partner Center y la ficha está preparada pero sin enviar (D:\sOCProjects\08-PENDIENTE-Uninstaller.md, puntos 6 y 7; Mobile/MicrosoftStore/Uninstaller/ficha-es-ES.md)
  - Edge Add-ons / Chrome / Firefox: no aplica
- descarga_alternativa: https://github.com/donki/Uninstaller/releases (última: v2026.09.22.02, con sOCUninstaller.exe, el zip y el MSIX de Windows; el último APK publicado ahí es el de v2026.09.19.07)

## Description

sOC Uninstaller is a batch uninstaller. Instead of removing apps one by one from settings, you see everything you have installed in a single list, check the ones you don't need and uninstall them one after another. It works on Android and Windows with the same idea and the same look.

On Android it shows each app with its icon, install date, last update and size, and you can sort or search them to quickly find what you no longer use. You confirm each uninstall yourself in the system dialog: the app never deletes anything on its own.

On Windows it puts classic programs and Microsoft Store apps together in a single list, and it can uninstall them without questions wherever the installer allows it. It also includes a **Disk space** tool to see which folders and files are eating up your disk, find duplicates and send what you don't need to the Recycle Bin.

## Main features

- List of installed apps with icon, name, install date, last update and size.
- Multiple selection with checkboxes and "Uninstall selected" in sequence, with progress ("2 of 5: name").
- Search by name or package (or publisher on Windows).
- Sort by install date, name, last update or size.
- Show or hide system apps.
- Windows: classic programs and Store apps in a single list, with unattended mode.
- Windows: Disk space with folder tree, treemap, largest files, breakdown by type and age, and duplicates.
- Windows: optional notification area icon and start with Windows.
- Light and dark mode; in Spanish and English.

## User guide (support)

### Getting started on Android

1. Install the app from Google Play and open it.
2. It won't ask you for any permission on screen. To work, it needs two permissions that are granted at install time: seeing the list of installed apps (to show it to you) and requesting uninstalls (to open the system uninstall dialog). It also connects to the internet, only to check whether there's a new version.
3. You'll see the list of your apps. By default only the ones you installed are shown; system apps stay hidden.

### Getting started on Windows

1. Download sOCUninstaller.exe (or the zip) from the GitHub releases. It's a single file: open it and you're done. The first time it takes a little longer because it sets itself up in your user folder.
2. If you want to keep it handy, pin the window to the taskbar: the pin keeps working after updates.
3. Some uninstallers will ask for administrator permission, as always on Windows.

### Everyday use

1. In "Installed apps", search or sort to find what you want to remove.
2. Check the box for each app (tapping the row checks it too).
3. Tap **Uninstall selected (N)** and confirm in "Uninstall apps" with **Continue**.
4. On Android, the system will ask you to confirm each one. On Windows, if any of them support silent uninstall, you'll be asked "Unattended?" first.
5. When it's done you'll see "N of M apps uninstalled" and the list refreshes with what's left.

### Side menu

- **Home**: the list of apps.
- **Disk space**: Windows only.
- **Settings**: language and, on Windows, tray and startup options.
- **About**: information about the app.

### Installed apps (Home)

Header:
- **Counter**: "N installed apps · N selected · by criterion". Tapping it also opens the sort menu.
- **Sort by**: Install date, Name (A–Z), Last updated and Size. The active criterion is checked.
- **Refresh**: reloads the list. You can also pull down to refresh.
- **Search**: shows the "Search by name or package" box. The counter reflects what's left in view.
- **Select all**: checks everything in view (if there's a search, only the filtered items).
- **Clear selection**: unchecks everything.
- **Show system apps**: shows or hides system apps (on Windows, Windows components). Your choice is remembered.
- **Disk space** (Windows only): opens the disk space tool.

List:
- Each row has the icon, the name, the package (on Windows, the publisher) and the detail "Inst. date · Upd. date · size", with the selection checkbox on the right.
- Empty list: "No apps to show. Pull to refresh or enable "Show system apps"."

Bottom button:
- **Uninstall selected (N)**: starts uninstalling everything checked. With nothing checked it warns "Select at least one app first.".

Uninstall dialogs:
- **Uninstall apps**: on Android, "You are about to uninstall N apps. Android will ask you to confirm each one."; on Windows, it explains that each program opens its own uninstaller and that Store apps are removed directly. **Continue** and **Cancel** buttons.
- **Unattended?** (Windows only): tells you how many can be removed without questions (Windows Installer, Inno Setup, NSIS and Store apps). **Unattended** removes them silently; **With wizard** opens each one's wizard. The ones that don't support it open their wizard either way.
- **Progress**: "Uninstalling…", a bar and "n of N: name".

### Disk space (Windows only)

Scan bar:
- **Drive selector**: pick a drive (local or network).
- **Drive, folder or network path (\\server\share)**: type a path and press Enter.
- **Scan** (play): starts measuring. You'll see "Scanning… folders, files, size" and the tree keeps growing in the meantime.
- **Stop**: stops the scan and leaves what it has covered in view.

Views:
- **Folder tree**: each folder with its size, percentage of the parent folder, number of files and folders, and last modified date. It expands row by row. Folders that couldn't be read are marked.
- **Treemap (one tap selects, two open the folder)**: each folder is a rectangle proportional to the space it takes up.
- **Largest files**: the files that take up the most space, with their folder.
- **By file type**: how much space each extension takes up.
- **By age**: Modified in the last month, 1 to 6 months, 6 months to a year, 1 to 2 years, Older than 2 years.
- **Duplicate files**: groups of files with truly identical content, with how much you'd recover by keeping just one copy.

Actions (on the selected row or on everything checked with the checkboxes):
- **Up one level**: in the treemap, goes back to the parent folder.
- **Show in Explorer**: opens the folder or highlights the file in Windows File Explorer.
- **Copy path**: copies the path (or paths, one per line).
- **Move to Recycle Bin**: asks for confirmation and sends it to the Recycle Bin, with undo from Windows. With several items checked, they all go in a single operation. Anything that's already inside the Recycle Bin is **deleted permanently**, and you're warned that it can't be recovered.
- **Export to CSV**: saves the current view to a CSV file in your Documents folder.

Safety warnings:
- **System folder**: before deleting anything from Windows, Program Files, ProgramData, a user profile or the root of the drive, it explains the risk. The default button is Cancel; to go ahead you have to press **Continue anyway**.
- **No permission**: if something can't be deleted, it offers **Change permissions and retry** (Windows will ask for administrator permission).

### Settings

- **Language**: **Español** and **English** buttons; "Select your preferred language". The change applies right away.
- **Windows** (Windows only):
  - **Keep in the notification area when minimised** (switch): when you minimize, the window hides in the tray. Click the icon to bring it back; right-click for **Open** or **Exit**.
  - **Start with Windows** (switch): starts hidden in the notification area when you sign in.

### About

- Name, "Version X", "Uninstall several apps at once" and Socratic.
- **Contact**: button with the email address; "Tap to send an email".
- **Privacy**, **License** (MIT) and **Legal Notice** with "Use at your own risk".
- **Back**.

### Update notice

If there's a newer version: "Update available: A newer version (X) is available. You have Y. Do you want to update?", with **Update** and **Not now**.

## FAQ

**On Android I have to confirm each app. Can't I remove them all at once?**
No. Android doesn't let any app silently uninstall other apps: for security, the user confirms every uninstall. sOC Uninstaller saves you from hunting them down one by one.

**The app I'm looking for doesn't show up.**
It may be a system app. Tap "Show system apps" or use the search box.

**On Google Play I don't see the search, settings or progress.**
The production version on Google Play is the one from August 2026. The new one is in closed testing and will move to production once Google approves it. In the meantime, the new APK is available in the GitHub releases.

**On Windows, a program keeps asking me questions even though I chose "Unattended".**
Only installers that support it (Windows Installer, Inno Setup, NSIS and Store apps) are removed silently; the rest open their wizard. Windows may still ask for administrator permission.

**Disk space won't let me delete a folder.**
If it's a permissions issue, accept "Change permissions and retry" and grant administrator permission. If you get the "System folder" warning, think twice: deleting that could leave Windows or your programs unusable. To remove a program, uninstall it from Home.

**I sent something to the Recycle Bin by mistake.**
Restore it from the Windows Recycle Bin or with Ctrl+Z in File Explorer. Anything that was already in the Recycle Bin and that you deleted from the app can't be recovered.

**I can't find Disk space on my phone.**
It only exists on Windows. On Android it would need the all-files access permission, which the app doesn't request.

**Is it on the Microsoft Store?**
Not yet. Download the Windows version from the GitHub releases.

## Privacy

sOC Uninstaller reads the list of installed apps only to show it to you, and on Windows it goes through the folders you ask it to in order to measure disk space; none of that leaves your device. There are no accounts, ads or trackers, and the only internet connection is to check whether there's a new version.
