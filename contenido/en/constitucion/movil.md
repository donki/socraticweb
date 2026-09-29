# Mobile apps constitution
- slug: mobile
- documento: CONSTITUCION-MOBILE.md
- orden: 2
- actualizado: 2026-09-28
- lema: Signing, versions, permissions, Google Play rules, the back button and the two apps that use a server.

Extends the general constitution for the apps built with .NET MAUI. Each one targets **Android,
Windows or both**, from the same project. On Google Play there are File Manager, Hiker, Music
Player, PDF Reader, QuitSmoke, SMS Forwarder, TXT Reader and sOC Uninstaller, which is also on the
Microsoft Store. Task Manager is distributed outside Play and is the only one with a desktop client
and a server; Family Together, for family location sharing, is in development.

## 1. Structure

**What it says.** Each app has its own folder and its own repository. The signing setup and the
shared code live in a common folder that all of them point to with relative paths, so none of them
can be moved. The Google Play listings (texts, icon, feature graphic, screenshots) and the demo
videos Google asks for are kept separately.

**Why.** A single source for what is shared; and the listings and videos next to everything else,
so a release can be redone without hunting for them.

## 2. Signing

### 2.1 All with the same key as File Manager

**What it says.** All apps are signed with **the same key as File Manager**, with no upload keys of
their own. If one turns up signed with a different key, it is fixed to use the common one, never
the other way around. Old copies of keys lying around are not valid for signing: the only valid one
is the one the shared configuration points to.

**Why.** A single key to look after, and a single configuration that each project imports instead
of repeating it.

### 2.2 New apps: the common key from day one

**What it says.** Before uploading the first version of a new app, in Google Play Console you choose
to use **the same signing key as another app in the account: File Manager**. No new key is created.
This can only be done while the app has no version uploaded yet, and there is no way to do it from
a program: a person does it in the console.

**Why.** If a new app is left with the key Google generates, Play rejects the first package signed
with the common one ("that key already signs another app that users receive; create a different
one"), and retrying does not help. It happened with sOC Credentials (three attempts), Task Manager
and TDT Online.

### 2.3 Two inherited exceptions

**What it says.** Task Manager and TDT Online were registered with their own upload key before this
rule, and on Play it can no longer be changed. What they upload to Play goes with their own key;
what gets installed over a cable, with the common one. This is not to be repeated.

**Why.** It is written down so nobody tries to "fix" it and finds out that Play does not allow it.

### 2.4 The key must not be lost

**What it says.** The key's public certificate is exported and stored, and the password is not in
the repository: it is supplied at build time.

**Why.** If the key were lost, we would have to ask Google to reset the upload key, with the wait
that involves; with the certificate at hand, the request is immediate.

## 3. Versions

**What it says.** The internal version number follows the format **YYYYMMDDNN**: the date plus a
counter of the day's builds, **always with two digits** (2026090701, not 202609071). The visible
version, the same: 2026.09.07.01. The number only goes up, never down: before building for the
store, you check which one is published, and the project's number has to match the uploaded
package's.

**Why.** Android only requires the number to go up; reading it as a date is our own convenience.
But a one-digit counter breaks it: the day you reach build 13 you get a ten-digit number, and the
next day build 1 comes out with nine, that is, **smaller**. Android rejects it as if it were an
older version. It happened with Task Manager on September 7, 2026. With two digits there is room for
99 builds a day, and the number still fits within Android's maximum until the year 2099.

## 4. Permissions

**What it says.** We ask for **the bare minimum**, and each permission has to match a real, visible
feature. Permissions tied to a feature are explained in the Play listing. Restricted permissions
(SMS, call log, background location, installing packages, access to all files) need a declaration
in the console and, often, a video.

**Why.** Each permission is access to the user's data that has to be justified; and Google Play
requires it as a rule, not as a recommendation.

## 5. Google Play rules

### 5.1 SMS: only as the default messaging app

**What it says.** Using the send-SMS permission to forward messages is a use case Google
**prohibits**. The only valid route is for the app to be the **default SMS app**, with everything
that requires implementing. And an app that asks to be the default (for SMS, phone, browser...)
asks for that role **before any other permission**, and no screen asks for permissions at the same
time as that dialog. It is tested by removing the role and the permissions and opening the app:
only the role dialog should appear.

**Why.** Google Play rejected SMS Forwarder in September 2026 for this, with the same code it had
approved in August; and the first fix still asked for a permission at the same time as the role.

### 5.2 The target Android version is mandatory

**What it says.** No app is built or uploaded with a target Android version below the one Google
Play requires at that moment: today, **Android 16**, for new apps and for any update. It is set in
two places in the project that have to match, it is checked in the manifest the build generates
(that is what actually gets uploaded) and, before each release, you check whether Google has raised
the requirement.

**Why.** If it is left unset, the version depends on what is installed on the computer doing the
build: two apps were being built for an older version without anyone knowing, and they were fixed
in August 2026. Better to raise it **before** building than after the rejection.

### 5.3 Closed testing first

**What it says.** There is a closed testing track, with the same tester groups for all apps.

**Why.** Whatever breaks, breaks first in front of a few people who know they are testing.

### 5.4 Demo video with no cuts

**What it says.** When Google asks for a video, it is recorded with no cuts, showing the full flow
that justifies the permissions.

**Why.** It is what the reviewer needs to see to approve a sensitive permission; a video with cuts
looks like it is hiding something.

### 5.5 Console declarations that block the release

**What it says.** Some permissions let you upload the package but do not let you complete the
release until a form is filled in on the web console: **foreground services** (this affects Hiker,
which records routes that way, and will affect Music Player because of background music), the
**read-SMS permission** (what has SMS Forwarder blocked) and newly registered apps, which only
accept draft releases.

**Why.** It is not a bug in the publishing program but a Google rule, and the message says so
plainly; knowing this avoids wasting time looking for an error that does not exist.

### 5.6 Developer verification

**What it says.** For an app to be installable on a certified Android device, its package name has
to be registered to a developer with a verified identity. Google Play apps are covered when they
are registered, but you check once in the console that there are no warnings. If packages signed
with our own key are ever distributed outside Play, that key will have to be registered too.

**Why.** An unregistered package can mean removal from the store worldwide, even though the install
block is not yet enforced in Spain.

## 6. Publishing

**What it says.** Fixed order: bump the version, build the signed package, check the actual version
number in the generated manifest, upload it to the testing tracks, test on a real device and only
then move to production. Two notes about the Google Play programming interface: a review option
that some apps require and others forbid (try without it first), and updating the tester list
**replaces** it entirely, so you read the current one and merge.

**Why.** Each step guards against the next: checking the number before uploading avoids a
rejection, and testing before production keeps a bug from reaching everyone. The tester lesson was
learned by deleting them by accident.

## 7. Interface

### 7.1 Shared design and screens

**What it says.** The shared indigo design, our own dialogs, buttons with flat icons (never emoji),
an "About" screen that is the same in all of them (logo, version, contact, language, license) and,
in the ones that sync, who is signed in and with which account, with an option to sign out.

**Why.** Someone who uses one app in the catalog already knows their way around the others; and
knowing which account you are syncing with is part of privacy.

### 7.2 The back button

**What it says.** On any screen other than the home screen, back **returns to the previous one**,
just like the arrow at the top; if something is open on top (a menu, a dialog, a search box), that
closes first. On the home screen, the app **hides** without closing or asking, and when you come
back it is where you left it. It is tested on the phone, with the gesture and with the button, on
every screen.

**Why.** It is what anyone who uses Android expects. And there are two documented traps: if the
main activity intercepts the button, the screens never find out; and **Android 16 turns on
"predictive back"**, with which the button stops reaching the screens and the app closes from
anywhere. Until .NET MAUI supports it, it is turned off in the manifest. It does not show up in the
emulator with an older Android version: only on a real phone with Android 16 (it was discovered
with File Manager in September 2026).

## 8. Task Manager: account, server and encryption

It is the app with an account and a server, and its description has to match word for word the
privacy policy and the listing.

- **Sign-in with an account the user already has**, from Google or Microsoft, using the standard
  sign-in protocol (OAuth 2.0 with PKCE) against the provider itself. We never see the password.
  Microsoft sign-in is built but hidden until it is tested with a real account.
- **Server:** a managed database service, hosted in the United Kingdom. It is the only third party,
  and only as hosting.
- **What is stored:** tasks, lists, steps, attachments, profiles, groups and their members, and
  records of what was deleted (only identifier and date, no text).
- **What is encrypted:** titles, notes, tags, list and step names, attachment names and addresses,
  group name, nicknames, and from the profile the name, email and photo. With AES-256-GCM.
- **What is not encrypted, on purpose:** dates, flags, numbers, identifiers, the code for joining a
  group (it is what gets searched on) and the hash of its password (it has to be compared).
- **Authorization is checked on the server**, row by row. The app not asking for something protects
  nothing.
- **It keeps working without the server**: the data is also on the device; what you lose is sync.
- **Notification between devices is not instant**, and that is a decision: one pass every 30
  minutes plus the refresh button.

**Why.** It is the app in the catalog that handles the most personal data, so how it treats that
data is written down in detail so it can be looked up without opening the code. Instant
notifications would require Google's notification service and its associated project, and for a
to-do list it is not worth it.

## 9. Device testing

**What it says.** There is a reference phone and a reference tablet, and each app's test material
is kept organized. Two traps noted: some manufacturers, when installing over a cable, show a
confirmation dialog with a six-second countdown that denies itself, and the leftover error looks
like a permissions issue; and a locally signed package cannot be installed over the same app
installed from Google Play, because the signature is different: you have to uninstall first.

**Why.** These are errors that throw you off and waste a lot of time the first time; once written
down, the second time takes ten seconds.

## 10. Family Together: anonymous user, server, notifications and location

Family Together shares location within a closed family group. Its own rules:

- **Anonymous user** created when it is first opened: just a display name and, optionally, a
  picture. Linking Google or Microsoft is optional and serves to recover the user on a new phone;
  that link is verified on the server, recovering moves the groups to the new phone, two users are
  never merged, and an account already linked to someone else is rejected with a notice.
- **Server:** for now, a managed database service; the goal is our own installation of the same
  server (open source) in the cloud, in the European Union. **Without a daily backup outside the
  server it does not go to production**, only the secure web port is opened, admin access uses a
  key and the dashboards are not public. Without the server the app does not work, because its
  whole point is sharing.
- **Row-level permissions on every table**: each person only sees what belongs to their groups, and
  joining, approving, removing or recovering is only done through server functions that check the
  role of whoever asks. A test with a user from another group must return nothing.
- **Encryption:** group name, member names and pictures, zone names **and the coordinates too**,
  with the group key. That key **never passes through the server in the clear**: it goes from phone
  to phone encrypted with a key exchange (ECDH). The only things left unencrypted are dates,
  identifiers, battery and the invitation code.
- **One position for each group** you share with, encrypted with that group's key, and it is kept
  for **30 days**; after that it deletes itself.
- **Instant notifications** with Google's notification service, messaging only: messages carry only
  identifiers and the text is put together on the phone; recipients are worked out by the server
  when sending; each notification has an identifier to discard duplicates, and there are separate
  channels for SOS, zones and requests.
- **The map** uses a free map library **bundled inside the app** and an open map style that needs no
  key. No Google Maps and no Google Play services for the map.
- **Background location** with a foreground service: it is sent when you move more than 25 meters,
  inaccurate readings are discarded, and offline they are queued with their original time. There
  is a guide so the manufacturer's battery saver does not cut it off.
- **Only the last phone that signed in shares location**: when the user is recovered on another
  one, the previous one stops sending.
- **Permissions** (precise and background location, foreground service, notifications and camera to
  read the QR code), all declared in the console, with a video and explained in the listing.

**Why.** A family's location is among the most sensitive data there is. That is why even the
coordinates are encrypted (the database does not need them: zones are detected on the phone), the
server never sees the group key, and storing one position per group means pausing is enforced at
the source: what was recorded while paused for a group never reaches it. Notification messages
carry no text so that the service delivering them does not know what they say, and the map is
inside the app so it does not depend on loading it from outside.
