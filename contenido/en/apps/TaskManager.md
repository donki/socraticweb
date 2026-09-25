# Task Manager
- slug: taskmanager
- plataformas: Android (phone and tablet), Windows
- lema: Your tasks on your phone and your computer, with the same account.
- github: https://github.com/donki/TaskManager
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.taskmanager — solo en la pista de prueba cerrada (alpha); la página pública da 404 hasta que pase a producción, lo que exige antes 12 probadores durante 14 días (fuentes: D:\sOCProjects\06-PENDIENTE-TaskManager.md, store/google-play/ficha.md, README.md; comprobado el 2026-09-25 que la URL pública devuelve 404).
  - Microsoft Store (publicada): https://apps.microsoft.com/detail/9PHJK2391727 (enlace de Josep, 2026-09-25; ficha pública comprobada)
- descarga_alternativa: https://github.com/donki/TaskManager/releases (APK, EXE y MSIX de cada versión; última: v2026.09.23.00)

## Description

Task Manager is a to-do list that's truly on all your devices: you write a task on your phone and it shows up on your computer, and the other way around. It's built for everyday use: open it, jot down what needs doing and close it. Each task can have its own list, tags, dates, repetition, steps, links and attached files, and anything that can't wait gets pinned right to the top.

Besides your private lists, you can create groups to share lists with your family, your roommates or a team. To invite someone, just show them a QR code: they scan it with the app itself and they're in. When you complete a task, the app celebrates with a little animation.

You sign in with an account you already have, Google or Microsoft, and what you write is encrypted on your device before it leaves. If you'd rather not use an account, you can continue without one and your tasks stay on that device only. On Windows it lives next to the clock, with a quick panel that opens with a keyboard shortcut.

## Main features

- The same tasks on your phone and your PC, synced with your Google or Microsoft account.
- Your own lists and groups shared with other people, with QR code invitations.
- Each task with a list, notes, tags, planned date, due date, repetition, steps, links and attached files (including images pasted from the clipboard).
- "My tasks", "My lists", "Board" (to do, in progress and done) and "Calendar" views.
- Filters by status and by date, a row of tags and a search box that looks in titles, notes, tags, steps and attachments.
- Multi-select to mark as done, pin, tag, move or delete several tasks at once.
- Daily repetition, weekly on the days you choose, monthly or yearly.
- Daily reminder of what's left and a notice on the due date, with the option to repeat the reminder.
- On Windows: tray icon with the number of pending tasks and a quick panel with a shortcut (Ctrl+Alt+T by default).
- Text encrypted before it leaves your device; light and dark mode; Spanish and English.

## User guide (support)

### Getting started

1. Install the app (Android from Google Play or the APK on GitHub; Windows with the EXE or the MSIX on GitHub).
2. The **Your account** screen opens with three options:
   - **Continue with Google** / **Continue with Microsoft** (on Windows: **Sign in with Google** / **Sign in with Microsoft**): your provider's page opens, you sign in there and come back to the app. Your account name becomes your name in the app. The account is what lets your phone and your PC share the same lists, and it's what makes groups possible.
   - **Continue without an account**: tasks stay on that device only, with no syncing and no groups. If you uninstall the app, they're lost. You can sign in with an account later.
3. Permissions Android asks for, and only when they're needed:
   - **Notifications**: for the daily reminder of what's left and for tasks that are due. It's requested when you turn on "Remind me what is left". Without it, the app tells you that Android won't show notifications.
   - **Camera**: only to read the QR code of a group invitation; it's requested when you tap the scan button. Without it, you can type in the code and key by hand.
4. Each account has its own lists on the same device: switching from Google to Microsoft changes what you see, but doesn't delete anything from the other one.

### Everyday use

Type the task in the box at the top and tap the add button (or press Enter). Tap it to open its details and fill in whatever it needs (dates, tags, steps...). Mark it as done with the checkbox on its row. Use the filters and tags to see what matters to you at any given moment.

### Side menu (Android)

Items: **My tasks**, **Calendar**, **My lists**, **Board**, **My groups**, **Settings** and **About**.

### My tasks

- **Add a task for today**: box to type a new task and an add button. The task goes into the first list and opens so you can fill it in.
- **Search**: searches in titles, notes, tags, steps and attachments. The X clears the search.
- **Filters**: **Pending**, **Pinned**, **Done**, **All**, **Overdue**, **Start date before today**, **Start date today or later**, **Due date before today**, **Due date today or later**.
- **Tag row**: **All tags**, **No tag** and one for each tag that has something pending. Fixed on the left is the button that opens the **Tags** screen. Long-press a tag (right-click on Windows): **Delete tag**.
- On each row: done/pending checkbox; tapping the task opens its details. Press and hold a task to drag it and change its order.
- **Refresh** (at the top): syncs again.
- **Select several**: shows checkboxes on each row and a bar with **Mark done**, **Back to pending**, **Pin to the top** / **Unpin**, **Add tag** (pick an existing one or "Or write a new one"), **Move to list** and **Delete** (asks for confirmation; if any of them repeat, it asks **Only the selected** or **Whole series**). The X or **Clear selection** leaves the mode.
- Footer: "Showing X of Y pending · Z% done".

### Tags

All the tags in use, including those only on finished tasks, with "N unfinished · N in total". The trash can on each one removes it from all its tasks; if unfinished tasks have it, it asks first.

### Task details

- **Pinned**: keeps it right at the top. **In progress**: moves it to the middle column of the board. On Windows there's also **Done**.
- **What needs doing** (title, required: if it's missing you'll see "The task needs a title.").
- **List**: which list it belongs to.
- **Notes**.
- **Tags**: separated by commas (for example "home, urgent, work"). On Windows, an **Add tag** button.
- **Due date** and **Planned for** (the day you mean to do it, which doesn't have to be the deadline).
- **Repeat**: **Does not repeat**, **Every day**, **Every week** (choosing the days of the week), **Every month** (**Day of the month** or "Same day"), **Every year** (**Month** and day). A repeating task needs both a planned date and a due date: when you save, all the repetitions in that range are created (up to 500).
- **Links and files**: **Add link** (paste the address), **Add file**, **Paste from the clipboard** (image or copied files; on Windows also Ctrl+V). Tapping an attachment opens it (double-click on Windows); **Remove** deletes it. There's a maximum size per file.
- **Steps**: type "What the step says" and **Add step**. Each step can be checked off, edited (**Edit step**), deleted (**Delete step**) and dragged to reorder.
- At the top: **Save** (check mark) and **Delete task** (trash can). If the task repeats, it asks **Only this occurrence** or **The whole series**.

### Calendar

The month, with tasks on the day they're planned for. **Previous month** / **Next month** arrows; on Windows, **Back to today**. When you pick a day, the **New task for this day** box creates a task planned for that day. Tapping a task opens it (double-click on Windows).

### My lists

All your lists with how many tasks are left. The **+** button creates a **New list**; the trash can deletes it (if it has tasks it asks **What about its tasks?**: **Move them** to another list or **Delete them too**). Inside a list: **Add a task**, search box, done checkbox on each task, a button to add it to or remove it from "My Day", and the pencil at the top to **Rename list**.

### Board

Three columns: **To do**, **In progress** and **Done**, with the same filters and tags as "My tasks". **New task on the board** creates a task in to do (on Windows, the **Add as in progress** button creates it directly in progress). On Windows you drag a card to another column to change its status; on Android, you tap the card to change its status from its details, and long-press is used to reorder.

### My groups

- Buttons at the top: **New group** (+), **Join a group** (key), **Scan the QR code** and **Refresh**.
- **New group**: name (for example "Family, Flatmates, Project...") and a **Shared key** of at least 6 characters. It's created with a first list called "General".
- **Join a group**: **Group code (6 characters)** and the key; or **Scan the QR code** from the invitation. On Windows the QR code can be read **From an image**, **From the clipboard** or **From the screen**.
- In each group: **Invite someone** (issues a new key: the previous invitation stops working, but anyone already in is not affected) and shows the QR code with **Share** and **Copy code and key** (on Windows also **Send by email** and **Send on WhatsApp**); **New group list**; and a trash can, which asks **Leave: it stays for the other members** or **Delete for everyone, with its lists and tasks** (only the person who created it can delete it).

### Settings (Android)

- **Your account**: the account's photo, name and email and **Sign out** (with no account it goes back to the sign-in screen; to use another account, sign out and choose it afterwards). Without an account you'll see "No account · This device only".
- **Reminders**:
  - **Remind me what is left** (switch).
  - **Snooze the reminder**: **Do not repeat**, **15 minutes**, **30 minutes**, **1 hour**, **2 hours**, **4 hours**.
  - **Daily reminder time**: time of the daily summary. There's one notification a day with what's left in My Day and another for each task with a due date (at 9:00 that day).
- **Celebration**: **Vibrate on complete** and **Sound on complete** (sound will arrive with the unlockable themes).
- **Identity**: display name, "How your groups see you".

### About (Android and Windows)

Version, **Contact** (**Write to the author**), **Also available on** (a link to the Windows version from Android, and to Google Play and GitHub from Windows), **Language** (**Español** / **English**; applies right away), **Privacy**, **License** and **Legal notice**.

### Windows: tray and quick panel

- The app lives next to the clock; the icon has a red badge with the pending tasks in My Day. Left-click or the shortcut (**Ctrl+Alt+T** by default) opens the **quick panel** on top of any window, even a full-screen game. Icon menu: **Open quick panel**, **Exit**.
- In the panel: typing + Enter adds the task (**Add task (Enter)**), search box, **Refresh**, and buttons to **My tasks**, **Calendar**, **Settings**, **About** and **Open main window**.
- Main window with **My tasks**, **My lists**, **Board**, **Calendar** and **My groups** tabs.

### Settings (Windows)

- **Your account**: current account and **Sign out**. Each account has its own lists.
- **Language**: Español, English or System language.
- **Global shortcut (for example Ctrl+Alt+T)**: key combination that opens the quick panel. If another app is already using it, you're warned and the previous one is kept.
- **Start with Windows and stay in the tray**.
- **Remind me what is left** and **Snooze the reminder**.
- **Play a sound when a task is completed**.
- **Display name**.
- **Save** and **Cancel** buttons.

## FAQ

**I can't see the tasks I created on my PC on my phone.** Check that you've signed in with the same account (Google or Microsoft) on both: each account has its own lists, and "Continue without an account" doesn't sync. Tap **Refresh**.

**A repeating task won't let me save.** Repeating tasks need **Planned for** and **Due date**: they're the range in which the repetitions are created. A series stops at 500 tasks; when you reach the end, set a new due date.

**I deleted a repeating task and the others keep showing up.** When deleting, choose **The whole series** instead of **Only this occurrence**.

**I'm not getting reminders.** Turn on **Remind me what is left** in Settings and grant notification permission when Android asks (or in the app's Android settings).

**The keyboard shortcut doesn't open the panel on Windows.** If another app is already using that combination, Task Manager tells you. Change the shortcut in Settings.

**I can't delete a group.** Only the person who created it can delete it for everyone; everyone else can **Leave** the group.

**I invited someone and they say the invitation doesn't work.** Each **New invitation** changes the key and cancels the previous one. Send the latest one.

**I want to switch accounts.** Settings › **Sign out** and sign in with the other one. Nothing is lost: when you go back to the previous account, its lists are still there.

## Privacy

Tasks are stored on your device and, if you sign in with an account, they're synced with the app's server so they're the same on all your devices; the text you write is encrypted on your device before it's uploaded and can't be read on the server. Without an account, nothing leaves your device. There are no ads, trackers or analytics, and the app never sees your Google or Microsoft password.
