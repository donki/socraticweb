# File Manager
- slug: filemanager
- plataformas: Android
- lema: A light, private file explorer: copy, move, search and share, with no ads.
- github: https://github.com/donki/FileManager
- tiendas:
  - Google Play (producción): https://play.google.com/store/apps/details?id=com.socratic.filemanager (ficha pública accesible el 2026-09-25 con el título «File Manager: sin anuncios»; D:\sOCProjects\11-PENDIENTE-FileManager.md y Mobile/GooglePlayConsole/FileManager/ficha.md)
  - Microsoft Store: no publicada (no hay ficha en Mobile/MicrosoftStore ni versión para Windows)
  - Edge Add-ons / Chrome / Firefox: no aplica
- descarga_alternativa: https://github.com/donki/FileManager/releases (última: v2026.09.14.0, APK)

## Description

File Manager (in Spanish, "Gestor de Ficheros") is a file explorer for Android that doesn't spy on you or flood you with ads. It shows you the folders and files on your phone or tablet and lets you organize them: copy, move, rename, delete, create folders, open and share.

It's light and fast, with the essentials and no clutter. You can search by name in the current folder and all its subfolders, filter by type (images, video, audio, documents, APK, archives) and sort by name, date or size. With a long press you mark several items and act on all of them at once.

It has no ads, no purchases and no account. Everything happens on your device: the app only connects to the internet to let you know about a new version.

## Main features

- Folder navigation with a tappable path and a Back button that goes up one level.
- Icons by file type, plus the date, size and number of items for each entry.
- Copy, move, rename, delete and create folders.
- Multiple selection with a long press to copy, move or delete in bulk.
- When pasting, you choose between replacing or keeping both.
- Search by name in the current folder and its subfolders.
- Filter by type and sort by name, date or size.
- Opens each file with the right app (including installing APKs) and shares it with any app.
- Show or hide hidden files; optional confirmation before deleting.
- Light and dark mode; in Spanish and English.

## User guide (support)

### Getting started

1. Install the app from Google Play and open it.
2. You'll see the "Storage access required" screen. A file manager needs the **All files access** permission to see and organize your folders; Android doesn't grant it with a normal dialog, but from its settings.
3. Tap **Grant access**. The system screen will open: turn on the switch for File Manager and go back. The app detects it by itself and shows your files.
4. There's a second permission Android may ask you for later, **Install unknown apps**, only if you tap an APK file and want to install it. You confirm each installation yourself in the system dialog.
5. The language follows your phone's (Spanish or English; if it's another one, English). You can change it in "Settings".

### Everyday use

1. The list starts at "Internal storage". Tap a folder to open it and a file to open it.
2. To go up one level, use the arrow in the top bar, the Android Back button, or tap any part of the path shown under the bar.
3. To act on an item, tap its three dots (⋮). To act on several, press and hold one and keep marking the others.
4. After "Copy" or "Move", go to the destination folder and tap **Paste** in the bottom bar.

### Main screen

Top bar:
- **Back arrow**: goes up to the parent folder (it doesn't appear at the root).
- **Title**: "Internal storage" at the root or the folder name; below it, the number of items.
- **Magnifying glass (Search)**: shows the "Search in this folder…" box. Type and the files in the current folder and all its subfolders are searched by name (up to 500 results). If there are no matches: "No files match your search".
- **Three dots (More)**: opens the menu with:
  - **Select**: enters multiple selection mode.
  - **Filter by type**: All types, Images, Video, Audio, Documents, APK, Archives, Other.
  - **Sort by**: Name (A–Z), Name (Z–A), Date (newest first), Date (oldest first), Size (largest first), Size (smallest first). Folders always go first.
  - **Show hidden files** / **Hide hidden files**: shows or hides the ones that start with a dot.
  - **Refresh**: reads the folder again.
  - **Settings**: opens the settings.
  - **About**: opens the app information.
- **Navigation path**: each part of the path can be tapped to jump to that folder.

List:
- Each row shows the type icon, the name and, below it, the date and size (or the number of items if it's a folder).
- **Tap**: opens the folder or opens the file with the associated app. An APK opens the Android installer.
- **Long press**: enters selection mode with that item marked.
- **Three dots on each row**: menu with **Select**, **Open**, **Share** (files only), **Copy**, **Move**, **Rename**, **Details** and **Delete**.
  - **Rename**: asks for a "New name" with **Save** and **Cancel**.
  - **Details**: Name, Path, Type, Size (or Contents for folders) and Modified.
  - **Delete**: asks for confirmation if it's turned on in Settings. Deleting a folder deletes all its contents and can't be undone.
- **Empty folder**: "This folder is empty. Create a folder or paste files here".

Floating button:
- **Plus (+) (New folder)**: asks for a "Folder name" and creates it in the current folder.

Selection mode (selection top bar):
- **X**: leaves selection mode (also with the Back button).
- **Counter**: "N selected".
- **Select all**: marks everything that's shown.
- **Three dots**: **Copy**, **Move** or **Delete** the marked items. If none are marked: "Select some items first".
- Tapping a row marks or unmarks it.

Paste bar (appears after Copy or Move):
- Shows how many items you're carrying and whether you're going to copy or move them.
- **Paste**: drops them in the current folder. If one with the same name already exists, it asks "Item already exists" with **Replace**, **Keep both** or **Cancel**.
- **Cancel**: empties the clipboard.

### Settings

- **Language**: **Español** and **English** buttons. Note: "The app follows your device language and falls back to English when it is not supported." When you pick one, it applies right away and is remembered.
- **Display**:
  - **Show hidden files** (switch): shows files and folders whose name starts with a dot.
  - **Ask before deleting** (switch): shows a confirmation dialog before deleting anything.
- **Storage**:
  - **All files access**: status "Granted" or "Not granted".
  - **Open settings**: takes you to the system screen where the permission is granted or revoked.
- **About**: opens the information screen.

### About

- Name, "Version X", "Browse and manage the files on your device" and Socratic.
- **Contact**: button with the email address; "Tap to send an email".
- **Language**: **Español** and **English** buttons; "Select your preferred language".
- **Privacy**, **License** (MIT) and **Legal Notice** with "Use at your own risk".
- **Back**.

### Update notice

If there's a newer version: "Update available: A newer version (X) is available. You have Y. Do you want to update?", with **Update** and **Not now**.

## FAQ

**I can't see any files.**
The all files access permission is missing. Go to Settings › Storage › Open settings and turn on the switch for File Manager.

**A folder shows up empty but I know it has content.**
It's probably Android/data or Android/obb. Since Android 11 the system blocks them for all apps, even with all files access.

**When I tap a file it says "No app on this device can open this type of file."**
You don't have any app installed that can open that format. Install one (for example, a PDF reader or a player) and try again.

**It won't let me create or rename: "The name contains characters that are not allowed".**
Names can't contain \ / : * ? " < > |. There also can't be two items with the same name in the same folder.

**"A folder cannot be copied into itself."**
You're trying to paste a folder inside itself or one of its subfolders. Choose another destination.

**The selection bar covered the first item.**
This was fixed in version 2026.08.28. Update to the latest one.

**I can't see my hidden files.**
Turn them on in More › Show hidden files or in Settings › Display.

**I deleted something by mistake.**
Deleting is permanent: there's no recycle bin. Turn on "Ask before deleting" in Settings so it always asks you for confirmation.

## Privacy

File Manager uses access to your files only to show them to you and do what you ask; it doesn't upload them anywhere or collect statistics. There are no accounts, ads or trackers, and the only internet connection is to check whether there's a new version.
