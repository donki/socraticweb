# TXT Reader
- slug: txtreader
- plataformas: Android
- lema: Open and read text, logs, JSON and code instantly, with no ads and no accounts.
- github: https://github.com/donki/TXTReader
- tiendas:
  - Google Play (producción): https://play.google.com/store/apps/details?id=com.socratic.txtreader (ficha pública accesible el 2026-09-25; paquete en TXTReader.csproj y Mobile/GooglePlayConsole/TXTReader/ficha.md; la pista alpha de prueba cerrada también existe según GRUPOS-VERIFICADORES.md)
  - Microsoft Store: no publicada (no hay ficha en Mobile/MicrosoftStore ni versión para Windows)
  - Edge Add-ons / Chrome / Firefox: no aplica
- descarga_alternativa: https://github.com/donki/TXTReader/releases (última: v2026.09.14.0, APK)

## Description

TXT Reader is a fast, distraction-free text file reader for Android. It opens notes, lists, logs, configuration files, JSON, XML, CSV or Markdown and shows them exactly as they are, in a fixed-width font that keeps columns and indentation lined up.

It detects the file's encoding on its own, so accents and special characters display correctly even if the file comes from Windows, a server or another program. You can search the text with instant highlighting, adjust the font size, and select and copy passages.

You can open files from the app itself or from any other app with "Open with": your file manager, downloads, email or the cloud (OneDrive, Google Drive, Dropbox). It has no ads, doesn't ask for an account and doesn't need storage permissions.

## Main features

- Opens .txt, .log, .json, .xml, .gpx, .csv, .md, .ini, .cfg, .conf and other text files.
- Automatic encoding detection (UTF-8, UTF-16, UTF-32, Windows-1252, ISO-8859-1).
- Search in the text with yellow highlighting as you type.
- Adjustable font size with a slider (from 8 to 32 points).
- Select and copy text just like in a browser.
- Recent files list to reopen them with one tap.
- Works with "Open with" and "Share" from other apps and cloud services.
- Automatic light and dark mode; in Spanish and English.
- No ads, no account and no storage permissions.

## User guide (support)

### Getting started

1. Install the app from Google Play (or the APK from the GitHub releases).
2. Open it. It won't ask you for any permission: you pick files with the system file picker, which only gives access to the file you choose.
3. The language follows your phone's (Spanish or English). You can change it in "About" › "Language".
4. If you're online, it checks at startup whether there's a newer version and, if there is, lets you know (see "Update notice").

### Everyday use

1. On the main screen, tap "Select File" and choose the file in the system picker.
2. The text opens in the reader with the file name as the title.
3. Type in the search box to highlight matches, move the side slider to change the font size, and long-press to select and copy.
4. Tap Android's Back button to return to the main screen. The file stays in "Recent Files".

You can also open a file from another app with "Open with" › TXT Reader (or "Share" / "Export" in Google Drive and Dropbox).

### Side menu

It opens with the menu button in the top bar. It has:
- **Home**: goes back to the main screen.
- **About**: opens the information and language settings screen.
- The installed version is shown at the bottom of the menu.

### Main screen (TXT Reader)

- **Select File**: opens the system file picker, filtered to show only text files (and the ones Android can't classify, such as .gpx, .log or .ini). PDFs, images and videos don't show up.
- **Recent Files**: a card with the last 5 files you opened, newest first, with their name and the date and time you opened them. Tap one to open it again. If the file no longer exists, it's removed from the list and you'll see the notice "File deleted: The file no longer exists and has been removed from history.". If you haven't opened anything yet, you'll see "No recent files".
- **About**: opens the "About" screen.

### Text reader

- **Title**: the name of the open file.
- **Search in text...**: search box. As you type, all matches are highlighted in yellow. Clear the text to remove the highlighting.
- **Size slider (A+ / A-)**: vertical slider on the left. Drag it toward A+ to make the text bigger and toward A- to make it smaller (from 8 to 32 points; it starts at 14).
- **Text**: shown in a fixed-width font. Long-press to select and use the system menu to copy.
- **Back** (system button): goes back to the main screen.

### About

- **Header**: app name, "Version X", "Text file reader" and Socratic.
- **Contact**: button with the author's email address. "Tap to send an email" opens your email app.
- **Language**: **Español** and **English** buttons. "Select your preferred language". The change applies right away and is remembered.
- **Privacy**: a summary of what the app does with your data.
- **License**: "This app is free software distributed under the MIT license."
- **Legal Notice**: "as is" terms of use and the warning "Use at your own risk".
- **Back**: returns to the previous screen.

### Update notice

When you open the app, if there's a newer version you'll see "Update available: A newer version (X) is available. You have Y. Do you want to update?" with two buttons:
- **Update**: opens the download page.
- **Not now**: closes the notice until the next time you open the app.

## FAQ

**I can't find my file in the picker, or it's grayed out.**
The picker only shows text files. If your file has an unusual extension, make sure you have the latest version: since 2026.08.01, .gpx and other files Android can't classify are supported too.

**I get "Could not access the Google Drive / Dropbox / cloud storage file".**
The file isn't available offline. Check that you're online and have permission for the file; if it keeps happening, download it to your phone first and open it from there. In Dropbox, use "Export" and choose TXT Reader.

**A recent file has disappeared from the list.**
When you tapped it, the app found that it no longer exists (it was deleted or moved) and removed it from the history. Open it again with "Select File" from its new location.

**Accented or special characters look wrong.**
The encoding is detected automatically, but very short files or files with mixed encodings can throw it off. Save the file as UTF-8 from the program that created it and open it again.

**The text is too small or too big.**
Use the vertical A+ / A- slider in the reader. The size goes back to 14 points when you open another file.

**Where are the settings?**
There's no settings screen: the only thing you can configure is the language, which is in "About".

**I only see 5 recent files.**
That's the maximum; the oldest ones drop off automatically.

## Privacy

Files are read only on your phone; they aren't uploaded anywhere and the recent files list is stored on the device itself. The app has no accounts, ads or trackers, and it only connects to the internet to check whether there's a new version.
