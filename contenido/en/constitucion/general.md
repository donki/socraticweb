# General constitution
- slug: general
- documento: CONSTITUCION-GENERAL.md
- orden: 1
- actualizado: 2026-09-30
- lema: The top layer: what applies to the whole catalog and what has been learned along the way.

The general constitution is the rule common to **everything**: mobile apps, Windows programs, games,
and the web. Each category also has its own document, which extends it but never contradicts it.
Many rules carry in parentheses the real case that made them necessary; those are told here too.

## 1. Non-negotiable principles

### 1.1 MIT license and commercial use

**What it says.** All of our own code and **all** the libraries used must have a license that is
compatible with MIT and allows commercial use. If a library does not meet this, it is dropped and
another one is found, no discussion.

**Why.** The code is published so anyone can read it, reuse it, or improve it, including in a
commercial project. A single dependency with a more restrictive license would be enough to prevent
that. It happened with a speech synthesis engine whose license did not allow commercial use: it was
left out, and two others with open licenses are used instead.

### 1.2 No ads, no trackers, no analytics

**What it says.** No app carries ads, trackers, or analytics. Users are not measured, not profiled,
and nothing of theirs is sold. There is no exception, and there never will be. The only thing
allowed is **Google's notification service** (Firebase Cloud Messaging), and only that piece, when a
feature needs an alert to arrive instantly with the app closed: the SOS in Family Together. None of
the analytics or crash reporting modules, the messages carry data only, with no readable text, and
their use is stated in the privacy policy and on the store listing.

**Why.** The apps are free to use and are made to learn: there is nothing to profit from anyone's
data, and trust can only be lost once. The exception is kept to the minimum because an SOS cannot
wait, and even so the service that delivers it cannot see what the alert says: the text is put
together on the phone itself.

### 1.3 Privacy first: local by default

**What it says.** Everything is processed on the device, and the apps are used without an account.
Nothing leaves the device except what the user deliberately sets up and understands. If a
requirement clashes with this, privacy wins.

**Why.** What never leaves the device cannot be leaked, sold, or lost on someone else's server. It is
the simplest way to protect data: not having it.

### 1.4 Account and server, only when that is the feature

**What it says.** An app may ask for an account and store data on a server only when its reason for
existing is sharing the same thing across several devices or among several people. It is not granted
for convenience: if it would work just as well without an account, it goes without one. When it
applies:

- It uses an account the user **already has** (Google or Microsoft), never an account of ours.
- The user's text leaves **encrypted** (section 5): it is never readable on the server.
- It states clearly **what leaves and what for** on the sign-in screen, in the privacy policy, and on
  the store listing, and all three say the same thing.
- There are still no ads, trackers, or analytics.

Today there are two: **Task Manager**, because without an account there is no way to know that the
phone and the laptop belong to the same person, and **Family Together**, because seeing where each
member of a group is cannot exist without a server.

**Recorded exception: Family Together signs in without an account.** Instead of asking for a Google
or Microsoft account, the app creates an anonymous user on the server the first time it is opened,
without asking for anything. Linking it to Google or Microsoft is optional and only serves to
recover it on another phone.

**Why.** With an account the user already has, we never store passwords: there is nothing to guard
and nothing that can be stolen. The Family Together exception is allowed because each person uses a
single phone, and asking the whole family (children, grandparents) for an account would hold back
exactly what the app has to do. There are still no accounts or passwords of ours.

### 1.5 Free and complete

**What it says.** There are no paid features and no artificial limits.

**Why.** A cut-down version that pushes people to pay would be the opposite of the idea behind the
catalog: that anyone can use the apps freely.

## 2. Repository structure

**What it says.** The work is organized into four main folders (mobile, games, tools, and web) plus
one for test material. The mobile apps share a common folder with the signing setup and shared code
(the custom dialogs, for example), and they reference it with relative paths, so **taking an app out
of its folder breaks the build**. Organization files (tasks, ideas) live outside the repositories.

**Why.** Shared things have a single source: if each app carried its own copy of the signing setup or
the dialogs, the copies would end up different without anyone noticing.

## 3. Version control

### 3.1 Commit often

**What it says.** Every work session ends by saving the changes to version control.

**Why.** On August 1, 2026, ten hours of work were lost because the changes had not been saved when a
file operation failed.

### 3.2 One repository per project, and the constitution as a submodule

**What it says.** Each project has its own repository, and the constitution goes into each one as a
**submodule** (a link to its repository), not as a copy.

**Why.** A loose copy goes stale without anyone finding out; the submodule always points to the one
version that gets edited.

### 3.3 Secrets are never stored in the repository

**What it says.** Signing keys, passwords, and credential files are never uploaded. They are excluded
from version control and passed in at build time or from a local file.

**Why.** The repositories are public. A secret uploaded once stays in the history forever, even if it
is deleted later.

### 3.4 Commit messages in Spanish, with the what and the why

**What it says.** Messages are written in Spanish, in the imperative, and explain **what** changes
and **why**.

**Why.** A year from now, the what can be read in the code; the why only survives in the message.

### 3.5 No assistant is listed as an author

**What it says.** Changes are signed only by the person who publishes them. No artificial
intelligence assistant appears as an author or a contributor: not in commits, not in descriptions,
not in READMEs, not on store listings.

**Why.** The code belongs to the project, and the one who answers for it is the one who publishes it.
The fact that the apps are made with the help of artificial intelligence (the website says so openly)
does not change who is responsible. In September 2026 the history of every repository was rewritten
to remove those mentions.

## 4. Secrets

**What it says.** Passwords and keys **never** go in the repository or in the documentation. The
mobile apps are signed with a shared key whose password is supplied at build time, and the
credentials for publishing on Google Play are kept on the work computer, outside the repositories.

**Why.** With the signing key and its password, anyone could publish a fake version that phones
would accept as ours. With the publishing credentials, they could upload it to the store.

## 5. Data and databases

This applies to every app that stores user data on a server (those under principle 1.4). The idea
in one sentence: **if something has to leave the device, it leaves unreadable.**

### 5.1 The user's text travels encrypted

**What it says.** Every **free-text** field that goes up to a server (titles, notes, tags, names,
nicknames, addresses, profile) is encrypted on the device before uploading and decrypted when
downloading. The local database stays unencrypted.

**Why.** That way, whoever has access to the server (an administrator, a security breach) only sees
unreadable text. The local copy is on the user's device, which belongs to them, and it is where the
screens search, filter, and sort.

### 5.2 What the database needs to understand is not encrypted

**What it says.** Dates, yes/no values, numbers, identifiers, the codes used for searching, and the
hashes that have to be compared go unencrypted.

**Why.** They are what decides what gets downloaded, who wins when two devices change the same thing,
and who can see each row. Encrypting them does not make the app more discreet: it breaks it.

### 5.3 With which key

**What it says.** A person's things are encrypted with a key of their own; a group's things (its
data, its name, and its members' nicknames) with a group key.

**Why.** That is what lets the other members of the group read them, and only them.

### 5.4 A version mark up front

**What it says.** All encrypted text begins with a mark that says which version of the encryption
was used.

**Why.** It makes it possible to live alongside what was uploaded earlier without encryption, and to
change algorithms later without losing what came before: the app knows how to read each value.

### 5.5 No length limit on the server for an encrypted column

**What it says.** Columns that store encrypted text have no length cap.

**Why.** Encryption makes text longer (a header plus a third more for the encoding), and a single
value that goes over the cap makes the server reject the whole batch.

### 5.6 The server does not write user text

**What it says.** If a server function fills in any of the user's text fields on its own, that part
is removed from it.

**Why.** It would rewrite in plain text what the device had just encrypted.

### 5.7 When encryption starts, what was already uploaded is migrated

**What it says.** The first time encryption runs, everything of the user's that was already on the
server is rewritten once, a note is made that it is done, and the modification date is not touched.

**Why.** Otherwise the old data would stay readable. And if the date were touched, the other devices
would see a change that does not exist and would download everything again.

### 5.8 State how far it goes

**What it says.** Wherever encryption is implemented, it is written down what it protects and what
it does not.

**Why.** Out of honesty: a key derived from something the server also knows protects against anyone
who sees the table, but not against someone who has the table **and** that piece of information.
Writing it down avoids believing you are more protected than you are.

### 5.9 Syncing cannot fail silently

**What it says.** When the server rejects something, the reason is saved somewhere it can be read in
a published version, not just in a debug trace.

**Why.** On September 1, 2026, the upload queue was stuck for hours because of a length limit on the
server, and nothing said so.

## 6. User interface

### 6.1 Buttons with icons, not words

**What it says.** Every action has a recognizable icon; text goes along with it only when the icon is
ambiguous. This applies to mobile, desktop, games, and the web.

**Why.** An icon is understood in any language, takes up less space, and does not get cut off with
large text.

### 6.2 Icons are always flat

**What it says.** Line drawings in SVG, on a 24×24 canvas, with no fill, a thin stroke with rounded
ends, and a single color: the palette's indigo, white on colored backgrounds, and red for deleting.
**Never emoji**, nor colored icons, gradients, or shadows, and each action uses the same icon
throughout the app. The only exception with color is the flags in the language picker, also flat,
next to the language name; never the country letters ("ES", "US") or the flag emoji.

**Why.** Emoji change their drawing from phone to phone, get cut off with large text, and do not
follow the light or dark theme. And Windows does not draw flag emoji: it shows two loose letters.
That is why this website uses flags drawn as images.

### 6.3 A shared design system

**What it says.** Indigo palette, system font, rounded corners, and custom dialogs instead of the
system ones.

**Why.** All the apps are recognizable as part of the same family, and the custom dialogs follow the
app's theme and color, which the system ones do not.

### 6.4 Light and dark mode

**What it says.** Everything with an interface works in both modes.

**Why.** It is a user preference, and a screen that ignores dark mode is blinding at night or leaves
text invisible.

### 6.5 Accessibility

**What it says.** Enough contrast, touch targets of at least 48 dp, and text that can be enlarged.
With the system font set large, no text or icon may be cut off, and this is tested on a real device
with the text scale the person uses.

**Why.** Many people use large text, and that is exactly where screens that were only tested with
the default text size break.

### 6.6 Every password box has the eye button

**What it says.** Passwords, encryption passphrases, and codes always have, inside the box, a button
with an eye that switches between dots and text. On Windows, the standard password control cannot
show what was typed, so a custom one that overlays two boxes is used.

**Why.** It avoids mistakes when typing a long password without being able to check what was typed.

### 6.7 Every app shows what's new

**What it says.** There is a **What's new** screen with what changed in the last five versions,
written for the user and in both languages. It appears on its own the first time the app is opened
after an update, and afterward it can be opened from the menu or from "About".

**Why.** A new feature nobody knows about might as well not exist; and a change that is not explained
looks like a bug.

### 6.8 What was typed is never lost without warning

**What it says.** What is typed or pasted into a box is applied when leaving it and when saving, not
only when pressing Enter. If it is not valid, a warning is shown and it is not saved; it is never
discarded silently.

**Why.** In sOC Credentials, the pasted two-factor secret was lost when pressing "Save", and the user
thought the app could not read their code.

### 6.9 Errors in the user's language, with the reason and what to do

**What it says.** The user never sees a technical message or one in another language. Every
foreseeable error has its translated text, and a failure that prevents what was asked (connecting,
syncing, signing in) appears in an alert that says in one sentence the reason and what to do. The
technical details go to the log.

**Why.** sOC Credentials once showed an internal message in English from an encryption library, and a
twenty-line server error made the RC Manager window unusable. Neither of them told the reader
anything useful.

### 6.10 A setup guide in every app

**What it says.** Every app has a step-by-step guide with what needs to be set up to get the most out
of it: its main options and, if needed, system settings (permissions, autofill, default app, start
with the system...). Each step explains what it does, has a button that does it or opens the screen
where it is done, and shows whether it is done, pending, or optional, checking again on return. It
appears on its own once and afterward is opened from the menu; the buttons to move forward stay fixed
at the bottom.

**Why.** Many features depend on a setting hidden in another system screen. With the guide, nobody
misses a feature for not knowing where to turn it on; and with the fixed buttons, "Next" is visible
even when large text makes the content scroll.

### 6.11 Unlocking with the app's own password

**What it says.** Apps that open with their own password (a vault, for example) open on Windows with
that password or with the **"Trust this user and device"** option, without Windows Hello. That trust
applies only to that user on that device, and it says so: another user on the same computer, or
another computer, still needs the password. Turning it on asks for confirmation, and the password
window appears small, at the bottom right.

**Why.** It makes clear what is being trusted and to whom: the key stays protected by the system
account, not open to anyone who uses the computer.

### 6.12 A global error handler in every app

**What it says.** An unexpected error **never closes the app**: it is written to the log with full
detail, the user is warned in their language, and the app stays open. It is hooked up at startup,
before any window opens, at every point where an error can slip out (the interface thread, background
tasks, and those specific to each platform).

**Why.** The Microsoft Store rejected sOC Phone Mirror in September 2026 because it "closes after
starting": a failure while starting a tool bundled inside the package brought it down without a
trace, and there was nothing to catch it.

### 6.13 Names of other companies' products in the apps

**What it says.** Microsoft and Google products may be named in the apps' text, plus a few others
that are needed for it to make sense (a very widespread messaging app, a phone maker and its brands,
and the most used browsers). Everything else is described by what it is ("other password managers",
"the storage service"...), except for attributions required by a license. On the website the rule is
stricter: only Microsoft and Google.

**Why.** It avoids trademark and look-alike problems, and there is no need to name a product to
explain what a feature does.

## 7. Languages

**What it says.** Spanish and English at a minimum. No text is written inside the code: everything
goes through the translation service. A new language is first proposed in the ideas list.

**Why.** With the text outside the code, translating means filling in a table rather than hunting for
sentences throughout the program; and it avoids announcing a half-done language.

## 8. Quality and delivery

**What it says.** A task is **done** when:

- It builds with no new compiler warnings.
- The **automated test suite** passes in full, the change comes with its tests, and coverage does not
  drop (8.6).
- It has been tested on a real device, not just an emulator.
- If the app syncs, it has been tested **on two devices with the same account**.
- The text is in both languages.
- It is saved in version control and its documentation is up to date.
- Someone has checked whether **this website** needs updating (the app's page or its support guide),
  whether the change is big or small, and if needed it is published in the same cycle.
- Every app is on the website, unless its repository is private or it is unfinished.
- The version is published as a **GitHub release** with its packages (APK on Android; EXE and MSIX on
  Windows) and the changelog notes.
- Windows apps leave each version in their OneDrive folder, ready to run as is, with a file that
  explains what each thing is.

**Why.** Each item is a failure that already happened: on a single device you see nothing of what can
go wrong when syncing; on the emulator you do not see the changes in new Android versions; and an
option that gets renamed leaves the website's guide wrong if nobody checks it. The GitHub release is
what remains of each version and what can be linked to.

### 8.1 Where to get each app

**What it says.** The README of each repository starts with a "Where to get it" section with links to
its stores (Google Play, Microsoft Store) and to the GitHub releases, and it is updated in the same
change in which the app enters a new store.

**Why.** Anyone who arrives at the code should be able to install the app without searching.

### 8.2 Store listings in Spanish and English

**What it says.** Every app that goes to the Microsoft Store, and every browser extension that goes to
a store (the Edge one, the Chrome Web Store, and those of other browsers), has its listings inside
the repository, one in each language, ready to paste field by field. When two stores ask for the
same thing, one refers to the other. Screenshots are taken with the real code and **made-up data**,
never real data or other companies' brands. Both versions say the same thing and change in the same
commit that makes them outdated.

**Why.** A listing that promises a feature that no longer exists is misleading advertising: when sOC
Credentials stopped using Windows Hello, it also had to come out of its listings. And a single text to
maintain is less text that falls out of sync.

### 8.3 Desktop apps: a single instance, and the new one wins

**What it says.** If an app that only allows one window finds another one open **from an earlier
version**, it closes it and carries on. With another of the same version, it asks it to show itself
and waits for its answer; if none comes, it starts anyway. If two start at the same time, one waits
for the other. And when a new version is installed, the app is opened again and it is checked that
the one running is the new one.

**Why.** In sOC Credentials, after every update the browser reopened the old version in the
background, and opening the new one handed control to the old one: it happened three times in one
day.

### 8.4 Testing on the developer's computer

**What it says.** When testing on the same computer where the app is actually used, an **isolated test
mode** is used, only in development builds, with its own data and without registering with anything
shared (neither the browsers nor the system). A test can never reach real servers, accounts, or data,
and before each automated click it is checked which window is in front.

**Why.** The test instance of sOC Credentials clashed with the real one, and the real one's autofill
even filled it in with the master password. A stray click in RC Manager opened a real connection to
work servers.

### 8.5 Privacy policy in the repository

**What it says.** Every repository of a published app carries its privacy policy in Spanish and
English, which says the same as the listings: what data is collected (usually none), where it is
stored, and who it is shared with.

**Why.** The stores ask for an address with the policy from day one, and this way it exists even if
the app does not yet have its page in the catalog.

### 8.6 Automated test suite

**What it says.** Every app has an automated test suite that runs in full with a single command. It
tests the logic (services, calculations, formats, importers, encryption, that the Spanish and English
translations have the same keys...), not the interface; and so that the logic can be tested, it is
moved out of the screens into its own classes. They are real tests (results, edge cases, errors),
without touching real data, external networks, or servers. Each repository publishes in its README
three dated figures: **how many tests there are** (and how many pass), **how much of the code they
cover** (also across the whole app, which is the honest figure), and **how long** the suite takes.
Coverage of the whole app must reach **at least 90%** (the goal is 100%); until it does, every version
**raises** it, there is a written plan to get there, and it **never drops** without an explanation; a new
app starts at 90% already. **Every new feature comes with its tests**: logic tests in this suite and
at least one **end-to-end** test that goes through it in the interface as a user would (8.7), in the
same version. A
green suite is a condition for accepting a version. Those figures, together with the **development
time with LLM** (approximate hours), are also published on each app's page on this website and on its
catalog card, and they are updated in the same cycle as the README.

**Why.** Testing by hand does not scale: a change in one place breaks another that nobody looked at
again. With the suite, each version rechecks everything before it in seconds. Publishing the figures
forces you not to fool yourself: a coverage figure that only counts the easy-to-test code does not
say how much of the app is checked.

### 8.7 Automated UI tests

**What it says.** Besides the logic tests, every app with a user interface has tests that drive it
the way a person would: they open it, go through the menu, press back on every screen, switch
language, create and delete a test item and, on the phone, check that with large text no label
runs off the screen. On Android they use a free phone-automation tool, and on Windows another one
that relies on the system's accessibility layer. Every button that gets pressed has its own
identifier, so the tests do not depend on the text, which changes with the language. They never use
real data or accounts: on the phone, only on an emulator and without signing in; on the desktop, in
an isolated mode that connects to nothing. They run before every version that touches the interface,
and their count and time are published separately from the logic tests.

**Why.** Some bugs only show up when you use the app: a back button that closes it instead of going
back, a label that vanishes with large text, a screen that does not open. Checking that by hand in
every version of every app is slow and gets forgotten; automated, it is checked the same way every
time. It was first tried on one phone app and one desktop app, and gave the same result in three
runs in a row before it became a rule.

## 9. How tasks are recorded

**What it says.** Pending work is noted in working files outside the repositories, one per app,
separating what can be done from the computer from what needs a person (web consoles, the phone,
accounts), ordered from shortest to longest. **What is done is deleted, not crossed out**, and a file
that ends up empty is deleted. All of them carry the date of their last update.

**Why.** A list full of crossed-out items hides what is missing. The history of what was done is
already in the changelog and in each app's history.
