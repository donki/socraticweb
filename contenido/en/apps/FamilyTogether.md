# Family Together
- slug: familytogether
- plataformas: Android
- lema: Your family on the map, in a closed, end-to-end encrypted group.
- github: https://github.com/donki/FamilyTogether
- tiendas:
  - Google Play: no publicada (todavía no está en Play; el APK de cada versión va en las releases de GitHub, según el README del repositorio a 2026-09-29)
  - Microsoft Store: no publicada (solo Android)
- descarga_alternativa: https://github.com/donki/FamilyTogether/releases (última: v2026.09.28.00, APK)

## Description
Family Together lets the people in a closed group (your family, your friends) see where each other is. The map shows each member's last position with the time and their phone's battery level, and in the history you can see where each person went over the last 30 days, with the route snapped to the streets and the stops marked.

You can create zones (home, school, work) and choose whose arrivals and departures you want to be alerted about. The red button sends an SOS to your groups, with your position, even if sharing is paused. And when you want some privacy, you pause a group for an hour, until tomorrow or until you resume it.

No account or password is needed: the first time you open it you only choose the name others will see. Everything you write and your coordinates are encrypted on the phone with a key that only the group's phones have, so the server stores data it cannot read. Free to use, with no ads, no analytics and open source code.

## Main features
- Map with each group member's last position, with the time and battery level, or "Paused".
- Background location every time you move about 25 metres, even with the app closed; without a connection, positions are stored and sent later with their original time.
- Route history: the last 24 hours when you open it and any day of the last 30, by person, snapped to streets and paths on the phone itself, with long stops shown as a single point.
- Group zones with arrival and departure alerts, only for the people and zones you choose.
- SOS with a 3-second countdown to cancel it, to all your groups or the ones you tick, even when paused.
- Pause per group: 1 hour, 8 hours, until tomorrow, until a given time or until you resume it.
- Closed groups: invitation by code or QR that expires after 5 minutes, and entry approved by an admin.
- No account: anonymous user, with optional Google or Microsoft linking to recover it on another phone.
- Names, zones and coordinates end-to-end encrypted with the group key; delete your history whenever you like.
- In Spanish and English, with light and dark mode.

## User guide (support)

### Getting started
1. Download the APK of the latest version from the GitHub releases and install it (Android 8 or later). Android will ask you to allow installing apps from unknown sources for the browser or file manager you open it with.
2. Open Family Together. The **Welcome** screen explains **What Family Together does** and **What leaves your phone**. Under **How others will see you**, type **Your display name (required)** (it is what others see on the map; it can be a nickname) and, if you like, pick **Your photo or avatar (optional)** with **Choose photo**. Tap **Continue**.
3. The **Setup guide** ("Get your phone ready") opens, step by step. Each step has a button that does it or opens the Android screen where it is done, and shows whether it is **Done** or **Pending**:
   - **Precise location** (**Allow location**): choose "Precise location"; with approximate location no position would be sent.
   - **Allow all the time** (**Allow all the time**): Android does not offer it in a dialog; Settings opens and there you choose Permissions > Location > Allow all the time. Without it your group only sees you while the app is open.
   - **Notifications** (**Allow notifications**): for SOS alerts, zone alerts and join requests. While sharing, Android also shows a persistent notification, "Sharing your location".
   - **No battery restrictions** (**Exclude from battery optimisation**): if Android puts the app to sleep, your group stops seeing you and alerts arrive late.
   - **Autostart** (**Open the manufacturer's settings**, **Optional**): where to let the app start on its own if your phone comes with its own battery or autostart manager.
   - **All set**: tap **Finish**. You can come back to the guide any time from the menu.
4. Create a group or join one from **Groups**.

### Everyday use
- **Create a group and invite**: in **Groups**, **Create group**, type the name (for example, Family) and tap **Create**. Open the group and tap **Invite**: the other person scans the QR or types the code. When they use it, you get their request and approve it with **Approve**.
- **Join a group**: in **Groups**, **Join with a code** (8 letters and digits) or **Scan QR**. Your request stays in **My requests** until an admin approves it; then the group appears in **My groups** and on the map.
- **See your people**: in **Map** you choose the group and see each member. To see where someone has been, **History**.
- **Ask for help**: the red **SOS** button on the map.

### Side menu
- **Map**, **Groups**, **Zones**, **History**: the main screens.
- **Setup guide**: back to the permissions and battery guide.
- **Settings**, **What's new** and **About**.
- The installed version is shown at the bottom.

### Map screen
- **Choose a group**: the selector at the top, if you are in more than one.
- **Refresh** (arrows, top right): asks for the positions again.
- When it opens, the map centres on your position: your own marker (your photo or initial with your name) is where your phone is right now. The centre button (**Show everyone**) fits all the group's members in view.
- The map fills the screen. **Find a person** (the magnifying glass, bottom right, above SOS) opens the group list: each member with their avatar or initials and "N min ago · battery N%", **Paused** (with the end time, if any) or **No position yet**. Choosing someone closes the list and centres the map on them; from the list you can also **Show everyone**. Back, or tapping outside, closes it.
- **SOS** (red button): "Send an SOS to your groups".
- Banners that may appear at the top, with their button:
  - "Your location is not being shared…", "Your group only sees you while the app is open…" or "The service that shares your location is stopped…": **Open the guide** and complete the pending step.
  - "This phone does not have this group's key…": the key arrives by itself as soon as another member opens the app; **Request the key again** requests it again.
  - "An SOS is waiting to be sent": it retries by itself as soon as there is a connection.
- With no groups: **No groups yet** with the **Go to Groups** button.

### SOS screen
1. The countdown starts, **Sending SOS in** 3 seconds. "Tap Cancel if it was a mistake": **Cancel** sends nothing.
2. **To these groups**: all are ticked; untick the ones you don't want to alert. It is sent with your location even if you are paused.
3. When done, **SOS sent** ("The members of N group(s) have been alerted with your position"). Without a connection it stays **Pending, retrying** and is sent by itself when the connection returns, even if you close the app. With no GPS at that moment, your last known position is sent with its time.
4. **Back to the map**.
- The others get "SOS from <name>" and, when they tap it, see you on the map.

### Groups screen
- **My groups**: each group with your role (**Admin** or **Member**); tap it to open it.
- **My requests**: the ones waiting for approval ("Request waiting for an admin's approval").
- **Create group** (+): asks for the name, which only members see and which travels encrypted.
- **Join with a code**: type the 8-character code an admin gave you (no O, I, 0 or 1) and confirm.
- **Scan QR**: point the camera at the QR the admin is showing. Without camera permission you can type the code by hand.

### Group screen
- **Invite** (QR, at the top): opens the **Invite** screen.
- **Pending requests** (admins only): "Asked to join … ago", with **Approve** or **Reject**.
- **Members**: each with their role. An admin can **Make admin**, **Remove admin** and **Remove from group** (the person stops seeing the group right away and the group stops seeing their position). There is always at least one admin.
- **My location in this group**: **Sharing** or paused. **Pause** offers **1 hour**, **8 hours**, **Until tomorrow at 8:00**, **Until I resume it** and **Until a time…**; **Resume** ends it. While paused this group neither receives nor sees your positions; your other groups are not affected.
- **Leave the group**: you stop seeing it and it stops seeing you; to come back you will need a new invitation. If you are the only member, the group is deleted; if you are the only admin and there are other members, you must appoint another admin first.

### Invite screen
- The group's QR and code, with **Expires in** and the minutes left (each code works for 5 minutes). When it expires: "Expired: get another code".
- **Another code**: creates a new one. **Share the code**: sends it with the app you choose. **Close**.
- When someone uses it, you get "Request to join" to approve or reject it.

### Zones screen (Group zones)
- Choose the group at the top. Each zone shows its name and **Radius: N m**, with **Edit** and **Delete** (it is deleted for the whole group, along with its alerts).
- **New zone** (+): type the **Zone name** (for example, Home), tap the map to set the centre and adjust the radius with the slider (50 to 2000 m). **Save**.
- **Alerts** (bell): opens the group's alerts screen.

### Alerts screen
- For each person in the group and each zone, two switches: **On arrival** and **On departure**. You will only be alerted about what you turn on here (for example, "Anna arrived at Home").

### History screen
- Choose the group and the **Person**. It opens on **Last 24 hours** (from this time yesterday until now, even across midnight); for an earlier day, choose **One day** and the date (the last 30 days are kept; anything older is deleted automatically).
- Your own route for the last 24 hours is also kept on your phone, so you can see it without a connection; it is deleted automatically after a day.
- The route is drawn on the map with **Start** (green), **End** (red) and each **Stop** (a stay of 10 minutes or more in the same place; tap it for "Stopped from … to …"). Below, "N positions, from … to …" ("yesterday 21:09" if it starts the day before).
- If the setting is on, you will see "Snapping the route to streets and paths…" and then whether it was snapped fully, partly, or drawn in straight lines because the map could not be looked up.
- **Delete my history** (bin, at the top): deletes your routes in all your groups, including those not sent yet. Your groups will still see your last position on the map. This cannot be undone.

### Settings screen
- **Language**: **System language**, **Español** or **English**. The change applies right away.
- **My name and avatar**: change your display name and photo (**Choose photo**, **Remove photo**); it is updated in all your groups.
- **Account**: shows whether it is linked. **Link Google** or **Link Microsoft** to be able to recover it. **Recover my account on this phone**: on a new phone with no groups, brings your groups, zones and history; the old phone stops sharing your location.
- **Permissions and battery**: the status of location (all the time / only while the app is open / no permission, and whether it is sharing or stopped), notifications and battery, with **Open the guide**.
- **History**: **Snap routes to streets and paths** (on by default; when off, no street map is looked up) and **Delete my history**.
- Shortcuts to **What's new** and **About**.

### What's new screen
- The changes in each version, with the installed one marked.

### About screen
- Name, version and author (Socratic).
- **Contact**: **Write to the author**.
- **Language**, **What's new** (**See what's new**), **Privacy** with **Privacy policy**, **License** (MIT) and the third-party libraries, and **Legal notice**: "Family Together is not a substitute for emergency services. In an emergency, call 112."

## FAQ
**Why is it not on Google Play?**
It has not been published there yet. The APK of each version is in the GitHub releases; you install it by hand, allowing apps from unknown sources.

**My group doesn't see me when the app is closed.**
Open the **Setup guide** and complete the pending steps: location must be set to "Allow all the time", notifications on and the app excluded from battery optimisation. Some brands also need **Autostart**. In **Settings › Permissions and battery** you can see the status of each one.

**I'm at home and my position doesn't change or looks approximate.**
Indoors GPS is weak and network location is imprecise. Those readings only update your last position on the map; they do not go into the history or trigger zone alerts. With the phone still, nothing is added to the history either.

**I see the group as "Group without a key on this phone".**
The phone does not yet have the key to decrypt that group (this happens when you join or recover your account). It arrives by itself as soon as another member opens the app; you can tap **Request the key again**.

**The invitation code doesn't work.**
Each code expires after 5 minutes. Ask the admin for **Another code**. It is 8 letters and digits, with no O, I, 0 or 1.

**I've changed phones. Do I lose my groups?**
If you linked Google or Microsoft on the old one, no: on the new one, before joining anything, go to **Settings › Account › Recover my account on this phone** with the same account. Without linking, reinstalling means starting as a new user.

**The history is drawn in straight lines instead of along the streets.**
Snapping needs a connection to look up the street map of the area. If it could not, the route is drawn straight with a notice. Also check that **Snap routes to streets and paths** is on in **Settings**.

**Can someone delete my history or see what I do while paused?**
No. Only you can delete your history, and whatever happens while a group is paused never reaches that group. SOS is still sent while paused.

**Does it replace calling emergency services?**
No. Positions depend on GPS, the network and the battery, and may arrive late or not at all. In an emergency, call 112.

## Privacy
There is no account or password: your user is anonymous, and only if you want do you link Google or Microsoft to recover it on another phone. Your position, the time and the battery level are shared with your groups when you move, and your coordinates, your name, your avatar and the names of groups and zones are end-to-end encrypted on the phone with the group key: the server stores data it cannot read. History is deleted automatically after 30 days and you can delete yours whenever you like. Notifications are carried by Google's notification service, with identifiers only, never your position or readable text. Routes snapped to the streets are computed on the phone: the map service is only asked for fixed areas of the map, never the route, and it can be turned off. No ads, no analytics and no trackers. The third parties involved are listed in the privacy policy.
