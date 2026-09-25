# sOC Credentials
- slug: credentials
- plataformas: Android, Windows, browser extension for Edge, Chrome and Firefox (on Windows)
- lema: Your passwords and verification codes, encrypted and yours alone, on your phone and PC.
- github: https://github.com/donki/Credentials
- tiendas:
  - Google Play (no publicada): la app todavía no está creada en Play Console; la URL prevista sería https://play.google.com/store/apps/details?id=com.socratic.credentials, que hoy da 404 (fuentes: D:\sOCProjects\09-PENDIENTE-Credentials.md punto 8, D:\sOCProjects\03-TAREAS-Credentials.md punto 1, README.md; comprobado el 2026-09-25).
  - Microsoft Store (no publicada): ficha preparada con el nombre «sOC Credentials», pero sin identificador de producto; el README dice «en cuanto Partner Center dé el enlace» (fuentes: README.md, store/microsoft/ficha-es-ES.md). Ojo: la versión de la Store no puede usar las extensiones de navegador; para eso hace falta la versión EXE de GitHub (README.md).
  - Edge Add-ons (publicada el 2026-09-24): https://microsoftedge.microsoft.com/addons/detail/soc-credentials/pcilggpjodagihemfbimfbnnmlbfhfbk (fuentes: 09-PENDIENTE-Credentials.md punto 7, CHANGELOG.md 2026.09.24.04, README.md; la URL responde 200 el 2026-09-25).
  - Chrome Web Store (no publicada): ficha preparada, falta la cuenta de desarrollador; sin ID (fuentes: 09-PENDIENTE-Credentials.md punto 7, store/chrome/ficha-es-ES.md).
  - Firefox Add-ons (no publicada): ficha preparada, sin enviar a AMO; sin ID de tienda (fuentes: 09-PENDIENTE-Credentials.md punto 7, store/firefox/ficha-es-ES.md). Hasta entonces, en Firefox solo se puede cargar como complemento temporal.
- descarga_alternativa: https://github.com/donki/Credentials/releases (APK, EXE/ZIP y MSIX de cada versión; última: v2026.09.25.03)

## Description

sOC Credentials keeps your passwords and your two-step verification codes in a vault encrypted with a single master password that only you know. There is no server of ours and no account with us: the vault lives on your device or, if you prefer, in the app's private folder inside your own Google Drive or OneDrive, always encrypted. That way you have the same passwords on your phone and your PC.

Besides storing them, it fills them in. On Android it becomes the system autofill service, offers you the right account in each app and in the browser, and suggests saving new ones. On Windows it fills in passwords in desktop programs and, with its extension for Edge, Chrome and Firefox, on websites too, including each site's verification code.

You can bring everything you already had: import from browsers, from other password managers and from verification code apps such as Google Authenticator. And no ads, no analytics, and an open-source license.

## Main features

- Vault encrypted with your master password, on the device or in your own Google Drive or OneDrive, synced automatically between devices.
- Four entry types: website, application, two-factor code and secure note, with folders, tags, favourites and extra fields.
- Live two-step verification codes (TOTP), added by pasting the link or the key, or by scanning the QR code; with the secret key, a QR code to move them to another app, and backup codes.
- Password generator and strength meter; history of previous passwords.
- Android autofill in apps and browsers, with an offer to save new ones.
- On Windows: filling in desktop apps and an extension for Edge, Chrome and Firefox.
- Import from Chrome, Edge, Firefox, Brave, Bitwarden, KeePass, Aegis, 2FAS and Google Authenticator; encrypted or plain-text export.
- Unlock with fingerprint or face on Android, and an option to trust the device.
- Lock after inactivity and automatic clipboard clearing.
- Step-by-step setup guide; Spanish and English.

## User guide (support)

### Getting started

1. Install the app (Android: APK from GitHub; Windows: EXE from GitHub, recommended if you want the browser extensions).
2. **Create your vault** screen: type a **Master password** (at least 8 characters) and **Repeat the master password**, then tap **Create**. It is the only key to everything: nobody can recover it, not even us. Write it down somewhere safe.
3. After the first unlock, the **Setup guide** opens by itself. Each step has a button that does it for you (or takes you to the system screen) and is marked **Done** automatically; optional steps are marked **Optional**. Buttons **Back**, **Next** and **Finish**. You can come back to it from the menu.
   - On Windows: **Always at hand** (start with Windows and stay next to the clock), **Passwords in apps** (turn on desktop autofill), **Extension for Edge / Chrome / Firefox** (one step for each installed browser), **Turn off the browser's manager** and **Your passwords on all your devices** (cloud).
   - On Android: **Autofill service**, **Preferred password service** (Android 14 or later), **Passwords in <browser>**, **Sign in with your fingerprint** and **Your passwords on all your devices**.
4. Permissions on Android: **camera**, only to scan two-factor QR codes (if you deny it, you can paste the code); **internet**, only if you keep the vault in the cloud. Android will also ask you to choose sOC Credentials as the autofill service.
5. If you want the vault in the cloud: **Settings › Where the vault lives** and choose **Google Drive** or **OneDrive**; sign in with your account and grant access to the app folder.
6. On another device: create the vault, sign in to the same cloud account from Settings and use the same master password. If the cloud copy was created with a different master password, the app asks you for it to merge them.

### Everyday use

Open the app and unlock it with the master password (or your fingerprint). Find the entry and copy the user name, the password or the code, or let autofill or the extension fill them in for you. When you sign up on a new site, accept "Save the … account in sOC Credentials?". On Windows the master password is asked once per session and the app stays next to the clock.

### Menu

**Vault** (home), **Settings**, **Setup guide** and **About**, with the version at the bottom.

### Unlock

**Master password** field with a button to show it, **Unlock** and, on Android if it is turned on, **Unlock with fingerprint or face**. On Windows it appears as a small window at the bottom right. If the password is wrong: "That is not the master password."

### Vault

- **Search title, user, site or tag**.
- **Sort by**: **Title**, **Last modified** or **Created**.
- **Lock**: closes the vault right away.
- **New** (+): choose the type, **Website**, **Application**, **Two-factor code** or **Secure note**.
- Filters in a row: **All**, **Favourites**, one per type, one per folder (with "/") and one per tag (with "#").
- On each entry: **Copy user name**, **Copy password**, **Copy 2FA code** and delete. Tapping it opens the details.
- If it is empty: "Add your first credential with + or import from a browser or another manager in Settings."

### Entry details

- **Favourite** (star) and entry type.
- **Title** (required), **User name or e-mail** (with copy), **Password** (with **Show** / **Hide**, copy and **Generate**) and strength bar: **Very weak**, **Weak**, **Fair**, **Strong**, **Very strong**.
- **Password generator**: **Length**, **Uppercase**, **Lowercase**, **Digits**, **Symbols**, **Avoid look-alike characters (0/O, 1/l)**, a button to generate another one, and **Use**.
- **Website (URL)** with **Open website**.
- **Two-factor code (TOTP)**: paste the **otpauth:// link or secret key** or tap **Scan QR**. Once the code is set, you see it live with its countdown, a copy button, remove, and **Show the secret key** (the secret key, with copy and its QR code to add it to another authenticator app).
- **Backup codes**: paste the ones the site gave you, one per line, and tap **Add codes**. They are shown with **Show the backup codes**; each one can be copied, deleted or marked as **Used**, and the top shows how many are still unused.
- **Folder**, **Tags, separated by commas**, **Notes**.
- **Extra fields**: **Add field** with **Name**, **Value** and **Hidden**.
- **Previous passwords**: history when you change the password.
- Creation and modification dates; **Delete** (it disappears from all your devices) and **Save** buttons. If you leave with changes, it asks "Save the changes before leaving?".

### Settings

- **Language**: **Español** / **English**.
- **Where the vault lives**: **Only on this device**, **Google Drive** or **OneDrive** (the active one is highlighted). With the cloud: "Signed in as …", **Sync now** and **Sign out**. Syncing is also automatic: when you open the vault, when you come back to the app, and every five minutes.
- **Security**:
  - **Trust this user on this device**: the vault opens by itself, without the master password, but only for your user on that device. It asks for confirmation (**Trust**); turn it on only if nobody else uses your user.
  - **Unlock with fingerprint or face** (Android): the key is only released after your fingerprint or face is verified.
  - **Lock after inactivity**: **Never**, 1, 2, 5, 10, 15, 30 or 60 min.
  - **Clear clipboard after**: **Never**, 15, 30, 60 or 120 s.
  - **Change master password**.
- **Import and export**:
  - **Import…**: CSV from Chrome, Edge, Firefox, Brave, Bitwarden or KeePass; JSON from Aegis, 2FAS or sOC Credentials. Duplicates are skipped.
  - **Scan Google Authenticator QR**: imports all the codes from that app's export QR code.
  - **Export encrypted vault**.
  - **Export as plain JSON (unencrypted!)**: asks for confirmation; keep the file safe and delete it when you are done.
- **Autofill** (Android):
  - Current status and **Use sOC Credentials to autofill** / **Change autofill service** (in charge in apps).
  - **Preferred password service** (Android 14+; it is the one Edge and Chrome follow).
  - **Open the browser settings**, with the steps to turn off the browser's own password manager.
  - **Offer it when unlocking**: while another manager is the autofill service.
- **Fill in Windows apps** (Windows): when you enter a password field in a program, the list of matching entries appears next to it; click one to type the user name and password.
- **Windows**:
  - **Keep in the notification area when minimised** (click the icon to bring it back; right-click for **Open** or **Exit**).
  - **Start with Windows**: asks for the master password once when you sign in, and asks again after you lock Windows (Win+L).
- **Browser extensions** (Windows): status per browser (**Installed** / **Not installed**) with **Install…**, and **Offer to install it when unlocking**. In Edge the store opens (click "Get" and "Add extension"); in Chrome, "Developer mode" and "Load unpacked" with the path already copied; in Firefox, "Load Temporary Add-on…" from about:debugging.
- **Danger zone**: **Delete this vault from the device** (you have to type DELETE; if it is not in the cloud, everything is lost).

### Browser extension (Edge, Chrome, Firefox)

- Icon in the toolbar: shows the entries for the site with **Fill**, **Copy username**, **Copy password** and **Copy code**, and **Search the vault…**.
- **Generate password**: **Length**, **Uppercase**, **Digits**, **Symbols**, **Generate** and **Use in page**.
- **Browser** section: switch "The browser saves and fills passwords", to turn the browser's own manager off or back on. The first time, it asks whether to turn it off (**Turn off the browser's** / **Keep it**).
- On the page: when you enter the user name or password, a list appears attached to the field; if you have typed something new, **Save what is typed in sOC Credentials**. When you submit a form it asks "Save the … account in sOC Credentials?" or "Update the password…?" with **Save** / **Update** / **Not now**. Right-click menu: **Fill with sOC Credentials**.
- It needs the Windows app installed; if the vault is closed, it warns "You need to open the vault in sOC Credentials".

### About

Version, description, **Contact**, **Privacy**, **License**, **Legal Notice** and **← Back**.

## FAQ

**I forgot my master password.** It cannot be recovered: it is the only key to the vault and nobody else has it. If you turned on **Trust this user on this device** or the fingerprint on any device, get in that way, export the vault and create a new one.

**What I save on my PC doesn't show up on my phone.** Both have to use the same Google Drive or OneDrive account (Settings › Where the vault lives) and the same master password. Tap **Sync now**. Since version 2026.09.25.03 syncing is automatic and the "OneDrive: 400 Invalid request" error is fixed.

**Edge or Chrome on my phone still offers Google instead of sOC Credentials.** On Android 14 and later, browsers follow the **Preferred password service**, not the autofill one. In Settings › Autofill, check all three places: the autofill service, the preferred service and the browser's own settings.

**The extension says it can't talk to sOC Credentials.** Open the app once: it registers the bridge with the browser by itself. If you have just updated, opening it is enough. Remember that the Microsoft Store version doesn't support the extensions; use the EXE version.

**In Firefox the extension disappears when I close the browser.** Until it is published in the Firefox store, it can only be loaded as a temporary add-on and has to be loaded again every time.

**I get "The copy in the cloud was created with a different master password".** Type the master password that copy was created with to merge it; your current password is kept.

**The browser offers to save the password twice.** Turn off its own manager from the extension icon (**Browser** section) or from the browser's settings.

**I can't scan the QR code.** Without camera permission it can't be scanned; paste the otpauth:// link or the secret key instead.

## Privacy

sOC Credentials doesn't collect any data: there is no server of its own, no accounts, no telemetry and no ads. The vault is encrypted on your device with your master password and only leaves it, encrypted, if you choose to keep it in your own Google Drive or OneDrive. The browser extension doesn't connect to the internet: it only talks to the app inside your computer.
