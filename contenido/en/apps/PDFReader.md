# PDF Reader
- slug: pdfreader
- plataformas: Android
- lema: Read your PDFs with no ads and no accounts: everything stays on your device.
- github: https://github.com/donki/PDFReader
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.pdfreader (solo en la pista alpha de prueba cerrada, sin producción, según D:\sOCProjects\02-PENDIENTE-PDFReader.md; la ficha pública devolvía «No se ha encontrado» el 2026-09-25, así que el enlace aún no sirve al público)
  - Microsoft Store: no publicada (no hay ficha en Mobile/MicrosoftStore; la versión de Windows existe en el código pero no se distribuye)
  - Edge Add-ons / Chrome / Firefox: no aplica
- descarga_alternativa: https://github.com/donki/PDFReader/releases (última: v2026.09.15.0, APK)

## Description

PDF Reader is a simple, private PDF reader for Android. It opens your documents, lets you swipe through pages, pinch to zoom and jump to any page you want, and it remembers where you left off in each one.

Every PDF you open is saved to a library of recent documents, along with its page count, its size and when you last read it. Tap it again and it opens on the last page you viewed. On Android 15 or later you can also search for text inside the document and open password-protected PDFs.

It has no ads, needs no account and doesn't ask for any storage permission: you pick files with the system file picker or open them from any app with "Open with".

## Main features

- Library of recent documents, sorted by last read.
- Pick up where you left off: each document reopens on the last page you viewed.
- Turn pages by swiping or with the previous and next buttons.
- Zoom by pinching, double-tapping or using the buttons, up to 4x, with sharp text.
- Jump straight to a specific page.
- Text search inside the document (Android 15 or later).
- Opens password-protected PDFs (Android 15 or later); the password is never saved.
- Opens PDFs from other apps with "Open with".
- Automatic light and dark mode; in Spanish and English.

## User guide (support)

### Getting started

1. Install the app. While it's in closed testing, you can get it through the Google Play tester invitation link or with the APK from the GitHub releases.
2. Open it. It won't ask for any permission: documents are chosen with the system file picker, which only gives access to the file you pick.
3. The language follows your phone's (Spanish if your phone is in Spanish; otherwise, English). You can change it in "About" › "Language".
4. If you're online, it checks for a newer version at startup and lets you know.

### Everyday use

1. In the library, tap "Open a PDF" and choose the file. You'll see "Opening document…" while it gets ready.
2. The document opens in the reader. Swipe left or right to turn pages, pinch to zoom and tap the page number to jump to another page.
3. Go back: the document stays in "Recent documents" and next time it will open on the same page.

You can also open a PDF from a file manager, your email or your browser with "Open with" › PDF Reader.

### Library

- **Header**: logo, "PDF Reader" and the tagline "Your documents, only on your device".
- **Info button (i)**: opens the "About" screen.
- **Recent documents**: list of the PDFs you've opened. Each card shows the name, the pages and size, and when it was last opened ("Today", "Yesterday" or the date). Tap a card to open it on the last page you read.
- **X button on each card (Remove)**: asks for confirmation with "Remove document: "name" will be removed from the library and from the app storage. The original file on your device is left untouched." Buttons **Remove** and **Cancel**.
- **Empty list**: if there's nothing yet, you'll see "No documents yet" and a hint to open your first PDF.
- **Open a PDF**: bottom button that opens the system file picker.

### Reader

Bottom bar, from left to right:
- **Left arrow (Previous)**: previous page.
- **Minus (Zoom out)**: zooms out.
- **Page number ("3 / 20")**: tap it to open "Go to page: Enter a number between 1 and N". Type the number and tap **Go**. If it isn't valid, you'll see "Invalid page".
- **Plus (Zoom in)**: zooms in, up to 4x.
- **Right arrow (Next)**: next page.
- **Magnifying glass (Search)**: opens the search bar. It only appears on Android 15 or later.

Gestures on the page:
- **Swipe left or right** (when not zoomed): goes to the next or previous page.
- **Pinch**: zooms in or out.
- **Double-tap**: zooms to 2x; another double-tap goes back to full-page size.
- **Drag** (when zoomed): moves the enlarged page around.

Search bar (Android 15 or later):
- **Search in the document**: type the text and press Enter. You'll see "Searching…" and then "1 of N" or "No results for "text"". If there are a huge number of matches, you'll be told "Showing the first N results.".
- **Up arrow / down arrow**: previous / next match.
- **X (Close search)**: closes the bar and clears the search.

### Protected PDF

When you open a password-protected PDF you'll see "Protected PDF: Enter the password for "name"." with a (hidden) password box and the buttons **Cancel** and **Open**. If it's wrong, you'll see "That password is not correct. Try again.". The password is not saved: you'll be asked for it every time you open that document.

### About

- **Header**: name, "Version X", tagline and Socratic.
- **Contact**: button with the email address; "Tap to send an email" opens your email app with a message ready to go.
- **Language**: **Español** and **English** buttons; "Select your preferred language". The change applies right away and is remembered.
- **Privacy**, **License** (MIT) and **Legal Notice** with "Use at your own risk".
- **Back**: returns to the library.

### Update notice

If there's a newer version: "Update available: There is a newer version (X). You have Y. Do you want to update?", with **Update** (opens the download page) and **Not now**.

## FAQ

**I can't see the search button.**
Text search requires Android 15 or later. On earlier versions the button doesn't appear.

**It says "Opening a password protected PDF requires Android 15 or later".**
Your Android version can't decrypt protected PDFs. Remove the password from the document with another program, or open it on a phone running Android 15 or later.

**"The selected file is not a valid PDF, or it is damaged."**
The file isn't a PDF or it's corrupted (for example, an incomplete download). Download it again and reopen it.

**A document has disappeared from the library.**
If you clear the app's data, the internal copy is lost and the entry is removed automatically ("The document is no longer available and was removed from the library."). Your original file is still intact: just open it again.

**If I remove a document from the library, is my PDF deleted?**
No. Only the copy the app keeps is deleted. The original file on your phone is left untouched.

**I can't find the app on Google Play.**
It's still in closed testing: it can only be seen through the tester invitation link. In the meantime you can install the APK from the GitHub releases.

**Can I edit, sign or annotate PDFs?**
No. PDF Reader is just a reader; those tools were tried out for a couple of days in September 2026 and then removed.

## Privacy

Documents are opened and stored only in the app's private folder on your phone; nothing leaves your device and PDF passwords are never saved. There are no accounts, ads or trackers; the only internet connection is to check whether a new version is available.
