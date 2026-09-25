# SMS Forwarder
- slug: smsforwarder
- plataformas: Android
- lema: Your SMS app that also forwards the messages you choose to another number.
- github: https://github.com/donki/SMSForwarder
- tiendas:
  - Google Play (producción): https://play.google.com/store/apps/details?id=com.socratic.smsforwarder — en la tienda aparece como «SMS Forwarder: Mensajes»; en producción está la 2026.09.22.2 y las 2026.09.23.8 / 2026.09.24.x están enviadas a revisión (fuente: D:\sOCProjects\TAREAS.md, entradas 2026.09.22.2 y 2026.09.24.0/.1 y apartado «SMS Forwarder no tiene fichero propio»; título comprobado en la página pública de Play el 2026-09-25; paquete en SMSForwarder.csproj)
  - Microsoft Store: no publicada (solo Android; no hay ficha ni ID de Store en el proyecto)
- descarga_alternativa: https://github.com/donki/SMSForwarder/releases

## Description
SMS Forwarder is a full-featured SMS app that you can set as your phone's messaging app: you receive, read, write, reply to and delete your SMS from it, with a notification in the notification bar every time a new one arrives.

Its standout feature is automatic forwarding, which is optional: you can have incoming SMS forwarded automatically to one or more numbers. It's perfect for not missing messages from a second line or a SIM you don't carry with you, or for making sure your bank codes also reach someone else. Each destination number decides what it gets: every SMS, only those from certain senders, only those containing certain words, or a combination.

Everything happens on your phone: no accounts, no servers, no ads, and the app doesn't even have internet access. Forwarded messages go out as regular SMS through your carrier.

## Main features
- Default SMS app: inbox and sent folder, a notification for every new SMS and quick SMS replies to incoming calls.
- Write, reply to and forward SMS manually, picking the recipient from the system contact picker.
- Detail view for each message with the full text, tappable links and buttons to copy the number or the text.
- Delete messages one by one or in bulk with multi-select.
- Automatic forwarding to one or more destination numbers.
- Filters per destination: every SMS, only from certain senders and/or only those containing certain words or phrases (ignoring case and accents).
- Set up forwarding for a sender in two taps, right from the message.
- Protection against forwarding loops.
- Diagnostics screen with permission status, help with battery and autostart settings, and an activity log.
- In Spanish and English.

## User guide (support)

### Getting started
1. Open the app. The first thing you'll see is Android asking whether to **use SMS Forwarder as your default SMS app**. Accept it: only the default app can receive, display, delete, mark as read and forward SMS. As the default app, Android grants it the SMS permissions without asking again.
2. Next, it will ask for permission to **show notifications**, which it uses to let you know about every SMS that arrives.
3. If it isn't the default app, you'll be asked separately for the **receive SMS** and **send SMS** permissions.
4. If you want to use automatic forwarding, open the side menu, go to **Settings** and add at least one destination number.
5. If your phone closes apps in the background (Xiaomi, Huawei, Oppo, some Samsung models...), go to **Diagnostics** and tap **Configure all permissions**, or **Battery** and **Autostart**, so forwarding keeps working with the screen off and after a restart.

The app doesn't ask for access to your contacts: when you pick a contact, the system picker opens and only passes along the number you choose.

### Everyday use
- SMS arrive in the **Messages** inbox and you get a notification with the sender and the text; tap it to open the app.
- If you have destination numbers set up, each incoming SMS is automatically forwarded only to the destinations whose conditions it meets, in the format "[SMSForwarder] De: sender" followed by the text.
- To write an SMS, tap **New message**; to reply to or forward a specific one, tap it in the inbox and use the buttons in the detail view.

### Side menu
- **Messages**: the inbox (start screen).
- **Settings**: language and forwarding destination numbers.
- **Diagnostics**: permissions, battery, autostart and activity log.
- **About**: version, contact, language, privacy, license and legal notice.
- The installed version appears at the bottom.

### Messages screen
- **"Make it your messaging app" notice**: only appears if SMS Forwarder isn't your default SMS app. It explains that without being the default it can't write, delete or mark messages as read. The **Set as default** button opens Android's prompt.
- **Inbox** / **Sent**: tabs to see the SMS you've received or the ones you've sent.
- **Select** (checkbox icon): enters multi-select mode.
- **Refresh** (arrows icon): reloads the list.
- **Message list**: each row shows the sender or recipient, the short date (the time if it's from today, otherwise the day) and the beginning of the text. Tap it to open the **detail view**; if the message was unread, it's marked as read.
- **Trash can** on each row: deletes that message from the phone after asking "Delete this message from the phone?" (**Yes** / **Cancel**).
- **New message**: opens the compose screen.
- If there's nothing there: "No messages" with the hint "The SMS you receive will show up here." (or "The SMS you send will show up here." in Sent).

**Multi-select mode**
- Each row shows a checkbox; tapping the row checks or unchecks it.
- At the bottom: a button to **select or deselect all**, **Delete (n)** to delete the checked ones (it asks "Delete n messages from the phone?") and **Cancel** (X icon) to leave the mode.
- Your phone's back button leaves multi-select mode instead of closing the app.
- If some can't be deleted, the rest are deleted and it tells you: "X of Y messages were deleted."

### Message detail screen (Message)
- **Sender** with a button to **copy the number** ("The number is on the clipboard.").
- **Full text** of the SMS. Web links are tappable and open in your browser.
- **Copy the text**: copies the whole message to the clipboard.
- **Forward**: asks "Who should this message be forwarded to?", offering your configured destination numbers or **Another recipient…**, and opens the compose screen with the text already filled in, preceded by "From: sender", so you can tweak it before sending.
- **Reply**: opens the compose screen with the sender already set as the recipient.
- **Auto-forward**: sets up who SMS from this sender will be forwarded to from now on:
  1. "Which number should get the SMS from X?": choose one of your destinations or **Another number…** (you have to type it; it must have between 7 and 15 digits).
  2. "What should Y get?": **Every SMS from X** or **Only the ones containing a word…** (you type the word or phrase; case and accents are ignored).
  3. If that destination was getting all your SMS, it warns you that from now on it will only get the ones that meet the condition.
  4. It ends with a confirmation like "Y will get the SMS from X" or "... containing "word"".

### New message screen
- **To**: phone number (for example +1 555 123 456) and a **contacts** button to pick it with the system picker.
- **Message**: the text, with a character counter out of 160 (what fits in one SMS).
- **Send**: sends the SMS ("Message sent"). It warns you if the number isn't valid ("Enter a valid phone number (7-15 digits)."), if the text is empty or if the SMS permission is missing.

### Settings screen
Header "Settings — Configure the numbers to forward SMS".
- **Language**: **Español** and **English** buttons; the active one is highlighted and the interface changes right away. On install, it uses Spanish if your phone is in Spanish and English otherwise.
- **Number field** ("E.g: +1 555 123 456") and **Add number** button: adds a destination you type in by hand. If it doesn't have between 7 and 15 digits it shows "Invalid number"; if it's already there, "Duplicate number".
- **Contacts**: opens the system contact picker and adds the chosen number ("Number added").
- **Configured numbers**: the list of destinations. Under each number there's a summary of what it gets ("Gets every SMS", or "Only from N sender(s) · with N word(s) or phrase(s)"). If it's empty: "No numbers configured" and forwarding is turned off.
  - Tap a number to open **Which SMS it receives**.
  - **Trash can** next to each number: deletes it after asking "Delete this number?" (**Yes, delete** / **Cancel**).
- **Information**: a reminder that incoming SMS are forwarded to these numbers, that you can add them by hand or from your contacts, that advanced permissions are in Diagnostics and that you delete them with the trash can.

### Which SMS it receives screen (for each destination number)
The number appears at the top. Everything is saved instantly, with no save button.
- **All SMS** (switch): when on, this number gets everything. When off, it only gets the SMS that meet the conditions below. Turning it back on clears the senders and the words.
- **Only from these senders**: add phone numbers by typing them and tapping **Add**, or with the **contacts** button. Empty means "from anyone"; with several, it's enough for the SMS to come from one of them. Numbers are compared by their last 9 digits, so it doesn't matter whether they arrive with or without the country code. Each sender has its own button to remove it.
- **Containing these words or phrases** ("E.g: code, invoice, order shipped"): add words or phrases with **Add**. Empty means "whatever it says"; with several, it's enough for one to appear; case and accents are ignored. Each one has its own button to remove it.
- If you fill in both lists, the SMS has to meet both: come from one of those senders **and** contain one of those words.
- If you try to add something that's already there: "That is already in the list."

### Diagnostics screen
Header "Diagnostics — System monitoring and status".
- **Permissions**: status of "Receive SMS" and "Send SMS" (it shows "Granted" if it's allowed and "Denied" if not).
- **Numbers**: how many destinations you have set up ("N numbers configured").
- **Permission Settings**:
  - **Check permission status**: checks the permissions again.
  - **Configure all permissions**: requests any missing permissions and the background settings; when it's done, it tells you whether everything is fine or whether something needs to be checked by hand.
  - **Battery**: checks whether the app is excluded from battery saving. If it isn't, it explains why and offers to open the system setting.
  - **Autostart**: opens the manufacturer's autostart settings; look for "SMS Forwarder" and turn it on so it works after a restart.
  - Notice: configuring all permissions makes sure it can receive and forward SMS even in the background.
- **Diagnostic Tools** › **Refresh status**: refreshes the permissions, the number of destinations and the log.
- **Activity log**: the latest things the app has done (forwards, errors, numbers added...). **Clear log** empties it.

### About screen
- Name, **Version** and author (Socratic).
- **Contact**: button with the email address; tapping it opens your email app.
- **Language**: **Español** / **English**, same as in Settings.
- **Privacy**, **License** (MIT) and **Legal Notice** ("Use at your own risk").

## FAQ
**My SMS aren't being forwarded.**
Check, in this order: that SMS Forwarder is your default SMS app (if it isn't, you'll see the notice with the **Set as default** button in Messages); that there's at least one number in **Settings › Configured numbers**; that the SMS meets that destination's conditions (tap the number to see them); and that in **Diagnostics** the permissions show as granted and the app is excluded from battery saving and has autostart enabled. The **Activity log** tells you whether the message was forwarded or why not.

**It stops forwarding with the screen off or after a restart.**
That's the manufacturer's battery saving. In **Diagnostics**, tap **Battery** and **Autostart** (or **Configure all permissions**) and turn on whatever it tells you to.

**I can't delete messages and they don't get marked as read.**
Android only allows the default SMS app to do that. Tap **Set as default** on the Messages screen.

**The forwarded SMS arrives cut off.**
Automatic forwarding sends a single 160-character SMS, with the header "[SMSForwarder] De: sender"; if the original text doesn't fit, it's cut and ends with "...". To send a long message in full, open it and use **Forward**, which lets you send the whole thing.

**A message isn't forwarded to a number that also texts me.**
That's the loop protection: SMS coming from one of your destination numbers aren't forwarded, and neither are those that already look like a forward (starting with "[SMSForwarder]", "From:", "Forwarded:" and the like). This stops two phones from forwarding messages to each other endlessly.

**Does forwarding cost money?**
Each forward is a regular SMS sent from your line, so it costs whatever your carrier charges for SMS.

**When I type a number, it says it isn't valid.**
It has to have between 7 and 15 digits. You can enter it with or without the country code and with spaces.

**I swiped a message or a number to delete it and nothing happens.**
Swiping no longer deletes: use the trash can button on each row, or multi-select mode to delete several messages at once.

## Privacy
SMS Forwarder reads and sends SMS only on your phone; the app has no permission to access the internet, there are no accounts or servers, and sOCratic never receives a copy of your messages. Your destination numbers and preferences are stored only on your device; the only data that leaves it is the forwarded SMS, which go through your carrier to the numbers you set up.
