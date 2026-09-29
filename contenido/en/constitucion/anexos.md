# Technical annexes
- slug: annexes
- documento: constitucion.md
- orden: 6
- actualizado: 2026-09-25
- lema: The exhaustive technical detail: the common core of any project and the annexes for mobile, desktop, server, native code, and design.

This is the technical document that sits beneath all the others. It started as the standard for
Android apps built with .NET MAUI and was then generalized: it has a **common core** (sections 1 to
24) that applies to any project and **annexes** with the detail for each platform. A project
complies by applying the core plus the annexes for the platforms it targets.

Some parts are older than the general constitution and do not always match it (for example, on the
flags in the language picker, on typography, or on signing keys). In that case **the general one
rules**, since it is the one that has been corrected with each lesson. An annex about a private
project is not explained here.

## Common core

### 1-2. Purpose and scope

**What it says.** It is the reference document for the architecture, security, publishing, and
maintenance of any project (mobile, desktop, server, web, or native code), from design through
maintenance. It leaves out product decisions and the requirements of each app.

**Why.** Separating what is common from what is specific lets a new project know from day one what
it has to comply with.

### 3. Non-negotiable principles

**What it says.** Privacy first (and, if an app shares data, the text leaves encrypted and
authorization is checked on the server); least privilege; secure by default (encryption on the
network, secrets outside the repository, no default passwords); no silent failures; every release
reproducible and verifiable from the code; a clean license; small, safe changes; and **stability
before improvement**.

**Why.** These are the ideas all the other rules come from: when a specific rule does not cover a
case, it is decided with these principles.

### 4. License, origin, and dependencies

**What it says.** Every project is published under the MIT license, with a license file at the root.
No code is copied under licenses that force the project's own license to change (the "copyleft"
ones, like the GPL); only dependencies with permissive licenses (MIT, BSD, Apache 2.0) or functions
of the operating system itself are used. Each dependency is recorded in a third-party inventory with
its use, its license, and its owner, and it is reviewed **before** being added.

**Why.** A copyleft license "infects" the project that includes it and would take away the freedom
of the MIT license from anyone who wants to reuse the code. The inventory makes it possible to know
at any moment what is inside and under what permission.

### 5. Project structure

**What it says.** Everything in its place: logic in services, never in the interface; data models
with no presentation logic; utilities that are pure and stateless; and anything platform-specific
wrapped in its own folder. What client and server share lives in a single module, services are
received through dependency injection, and no dead or duplicated code is left behind.

**Why.** Logic kept out of the interface can be tested and reused; and with a single source for
each thing, a fix is made once and not in three copies.

### 6. Security, secrets, and compliance

**What it says.** No credentials in the repository; the configuration that gets published has its
sensitive fields empty, and without credentials no access is allowed. Everything that travels over
the network is encrypted, and if it passes through intermediaries, it is encrypted end to end.
Passwords are stored as a hash, never in plain text. Every permission and every port is justified.
If the software can affect third parties (remote access, for example), there is a responsible-use
notice. Store texts are truthful, with no broken promises. And every app carries a visible **legal
notice**: it is provided "as is," without warranties, and its use is the responsibility of whoever
uses it.

**Why.** A default password is a published password. The legal notice is what comes with any free
software: it is given away as it is, and no one can answer for every use it is put to.

### 7. Presentation architecture

**What it says.** Interface and logic always separate: the code for each screen is thin and
delegates to services. Heavy presentation patterns are avoided when they do not add clear value,
and two styles are not mixed for the same kind of screen.

**Why.** The simplest solution that separates things well is the easiest to read and maintain; a
heavy pattern only pays off when it solves a problem that actually exists.

### 8. Languages

**What it says.** No visible text written in the code: everything comes from a translation catalog.
If a translation is missing, the default language is used, **never** the internal key. Only the
languages that are truly translated are advertised. The chosen language is saved and, the first
time, the system's language is respected. Dates and numbers use the user's format. Spanish and
English always, also in the store listing, the privacy policy, the release notes, and the legal
notice.

**Why.** Showing a text's internal key or a half-translated language makes the app look broken; and
respecting the system's language saves people from having to hunt for how to change it.

### 9. Data

**What it says.** The user's data is stored on their device or on a server under their control;
each piece of data in the storage that fits it; no secrets in plain text; missing or damaged data is
handled without silent failures; and there is a plan for migrating the format between versions. It
also repeats, in detail, the encryption of the user's text from the general constitution (section
5): what is encrypted, what is not, with which key, the version marker, and the migration.

**Why.** The same reasons as in the general constitution: what leaves the device leaves unreadable,
and what the database needs to understand is not encrypted.

### 10. Errors and logging

**What it says.** Failing silently is forbidden. Whatever can fail (files, network, platform) is
guarded with clear messages. Debug traces only in development builds, no personal data or secrets
in the logs, and log files kept outside the repository. On servers, logs that rotate so they do not
fill the disk. And **never wait on a task by blocking the interface thread**.

**Why.** The last one was learned like this: sOC Credentials would hang on startup, with a black
window, as soon as there was a saved key, because the interface was waiting on a task that in turn
needed the interface to finish.

### 11. Versions

**What it says.** A single scheme across the whole project, defined in one place: the date plus a
two-digit counter for the day (YYYY.MM.DD.NN), or a semantic version when a store requires it. The
readable version and the internal code go up together, with a script, and every version is recorded
in the changelog.

**Why.** Looking at the version tells you which day it is from; and with a single source, no two
components report different versions.

### 12. Building and packaging

**What it says.** Scripts kept in the repository build, package, and sign, so that any version can
be regenerated from the code. Self-contained packages when they reduce dependencies; a single script
if the project mixes several languages; signing with the material kept outside the repository; and
the build free of errors, with warnings being phased out.

**Why.** If a project can only be built on one specific computer and from memory, an old version
cannot be rebuilt when it is needed.

### 13. Distribution and publishing

**What it says.** First a restricted channel (closed testing or a partial rollout) and only then
everyone. Packages are verified by their fingerprint (SHA-256) before being installed. Store texts
are consistent across all languages. And behavior changes are not mixed in the same release with
changes to listing texts only.

**Why.** A bug that reaches few people gets fixed without harm; the fingerprint guarantees that what
is installed is what was published; and keeping changes separate shows what caused a problem.

### 14. Servers and services

**What it says.** With a third-party managed service: the schema as code in the repository, only the
public key in the client, and row-level authorization in the service. With your own server: it is
installed as a system service that starts on its own, the configuration sits next to the program
with no secrets, the addresses it advertises are reachable from outside, deployment is automatic
with its credentials stored as secrets of the integration system, and when it finishes, it is
checked that the server responds with the expected version.

**Why.** What is done by hand on a server cannot be repeated or reviewed; and advertising a
home-network address means no outside client can connect.

### 15. Version check and updating

**What it says.** On startup, the app checks, without blocking and silently if there is nothing, if
a different version exists. If there is one, **it offers it to the user**, who decides; it never
updates without their permission. It is downloaded from a trusted source, the fingerprint is
verified, the configuration is kept, and for automatic updates the downloads are staggered so the
server is not overloaded.

**Why.** People using the app need to be able to know there is a better version without having it
forced on them.

### 16. Quality

**What it says.** No build errors; unit and integration tests when feasible, and end-to-end tests in
distributed systems; permissions and ports justified; every change verified in a real environment;
README and changelog up to date.

**Why.** Building is not working: only testing for real shows what the compiler cannot see.

### 17. Publishing flow

**What it says.** Seven steps: bump the version, update the changelog (and check that the
constitution is up to date), build and sign with the script, validate the output, publish to a
restricted channel, go through the channel's checklist and, finally, move to production and tag the
version in the repository.

**Why.** A fixed order means no step gets skipped in a hurry.

### 18. Contingency plan

**What it says.** What to do about the usual errors: a stuck build (close processes and clean), a
rejected version number (bump it), a locked default language, signing problems (check key, password,
and alias), credential failures when publishing, and failures when deploying a server.

**Why.** When something breaks in a hurry, having the recipe written down saves the time of
remembering how it was fixed last time.

### 19. Definition of "done"

**What it says.** A version is ready when it builds and signs correctly, publishes without errors,
the icon shows, the texts are in every language, the permissions are justified, the changelog and
version are up to date, it has been tested for real, and it carries the legal notice.

**Why.** It is the list all the lists in the general constitution come from: without it, "done"
means something different every day.

### 20. Collaboration in the repository

**What it says.** One logical change per commit, messages that say what and why, no mixing of
behavior changes with style changes, one branch per task, reviews with a description and impact,
and documentation kept up to date.

**Why.** A clean history makes it possible to understand, undo, or review each change on its own.

### 21. Continuous improvement

**What it says.** The code is reviewed from time to time and improved in small steps, but
**stability is never sacrificed for an improvement**: every change leaves the product working and
checked, in its own commit, without changing what the user sees. Anything big is planned as a
separate feature.

**Why.** An app that works a little worse but works is better than a prettier one that does not
start.

### 22. Naming and code style

**What it says.** A single language for code and comments in each project, the usual naming
conventions of each programming language, shared styles instead of repeated values, and descriptive
names instead of abbreviations.

**Why.** Code is read many more times than it is written.

### 23. The constitution as a submodule

**What it says.** The constitution lives in its own repository and each project includes it as a
submodule, which is read-only inside the project. Improvements are proposed in the original
repository; anything specific to a project goes in its README. Each project points to a specific
version and updates it on purpose, and when publishing, it is checked that it has not fallen behind.

**Why.** An edited copy inside a project is a divergence, not a version; and staying pinned without
review makes a project break rules that have already been learned.

### 24. Visual design system

**What it says.** **One visible value, one source**: no color, size, or radius is written loose on a
screen; everything comes from a color named by its role ("Primary," not "Blue") or from a named
style. Every background or text color has its light and dark pair. There is a minimum set of styles
(card, title, text, primary and secondary button), controls declare their states (a disabled button
has to look disabled), touch targets are at least 48 dp, and each app sets its scale once.

**Why.** It lists the mistakes that were actually seen: style dictionaries nobody loaded, the default
template published untouched, dark mode accidentally cancelled by setting a light color on every
screen, several palettes mixed together from copying screens from different projects. A loose color
is a decision nobody can ever find again.

## Annex A: mobile and stores

### A.1 Structure and targets

**What it says.** Fixed folders for screens, services, models, and resources, and anything
platform-specific in its own. Each app declares whether it targets **Android, Windows, or both**,
with the same project: whatever depends on the platform sits behind a service with one
implementation for each. No rule is relaxed because of the platform. On Windows it is delivered as
EXE and MSIX and published on the Microsoft Store; on Android, on Google Play.

**Why.** A single project for both platforms is a single place to fix each bug.

### A.2 Package identifier

**What it says.** They all follow the same format (com.socratic.name), in lowercase.

**Why.** It is public and **cannot be changed** once published: it is worth getting it right the
first time.

### A.3 Android permissions

**What it says.** The manifest is reviewed before each release, each permission is justified, the
ones modern Android versions no longer need are not requested (better to use the features that do
not require permission, like the system file picker), the ones that are only needed on old versions
are limited to those versions, and the ones that come with the project template and are not used
are removed.

**Why.** An inherited, unused permission breaks least privilege just as much as one added by hand.

### A.4 Versions for the store

**What it says.** The readable version with the date and the internal code with the two-digit
counter for the day, updated together on every build.

**Why.** With a single digit, on a day with more than nine builds the next day's number comes out
lower and the install is rejected.

### A.5 Google Play

**What it says.** Closed testing, internal testing, and production tracks; always closed testing
first, and to production only with complete texts and permissions. A legible icon and consistent
texts in every language.

**Why.** It is what Google asks for, and what keeps a bug from reaching everyone at once.

### A.6 Mobile publishing flow

**What it says.** Version, changelog, build and sign, validate the package, publish with the script,
check in the console (version, track, icon, language, texts), and tag the version in the
repository.

**Why.** The general flow (section 17) applied to Google Play.

### A.7 Packages with everything inside

**What it says.** Every package that gets installed, test ones included, carries all its pieces
inside; none of the fast development deployment, which leaves them out.

**Why.** Installed by hand, a package like that crashes on startup because it cannot find its
pieces.

### A.8 Mobile validation

**What it says.** For day-to-day work, an Android emulator for PC that starts quickly is used, with a
script that installs and opens the app, rules for opening it without touching anything else,
checking that the window in front is ours, and checking that startup leaves no error in the log. But
that emulator runs an old version of Android and **does not replace** the real device: before
publishing, the app is tested on a real one or on an emulator with the target version. Cold start,
light and dark theme, every language, and the empty and error states are checked, always with
**made-up data**, never personal data.

**Why.** A screenshot that "looks fine" can hide an error that was already logged; and changes in
new Android versions only show up on them.

### A.9 Design in .NET MAUI

**What it says.** The reference is Task Manager: when in doubt, do it the way it does. Colors and
styles live in two files that are actually loaded at startup, the default style template is
replaced (not left alongside), cards use the modern control and not the obsolete one, no screen sets
its own background color, buttons declare their disabled state, icons are line-style and vector
(never emoji), and texts come from the translation service. They all have the same "About" screen
(icon, version, contact, language, privacy, license, and legal notice), **no donations** anywhere,
and a side menu with, at a minimum, Home and About, each option with its icon. System typography,
except in games.

**Why.** A cheap check is included: if renaming a style does not break the app, that file was not
being loaded. The donations point was clarified after a contradiction between two sections that
explained why some apps had them and others did not: the ban rules.

## Annex B: desktop

### B.1 Interface

**What it says.** The Windows windowing technologies (WinForms, WPF, WinUI), with thin code for each
screen and the system's light or dark theme when possible.

**Why.** The same reasons as section 7.

### B.2 Third-party control libraries

**What it says.** **Individual controls are taken, never the full theme** of a third-party library.
One MIT-licensed control library is allowed only for three controls that do not exist out of the
box (tags, in-window notifications, and a time picker), and only its pieces are imported, recorded
in the third-party inventory.

**Why.** A full theme imposes its own identity and restyles the standard controls, so it clashes
with our own design; and when the app has a sibling on mobile, the desktop version has to look like
it, not like the library.

### B.3 Packaging

**What it says.** Installer or ZIP with a reproducible script, native code included, and system
integration (automatic startup, tray) at the user's choice.

**Why.** What gets installed has to be regenerable, and what stays in the system is decided by the
person who uses the computer.

### B.4 Updating

**What it says.** Updating replaces the program and restarts it, keeping the configuration and
verifying the package's fingerprint.

**Why.** Updating cannot cost the user their settings.

## Annex C: web and servers

**What it says.** A service with its user registration, authentication, and dashboard depending on
the project, and the models shared with the clients. Always over HTTPS, token authentication,
passwords as a hash, end-to-end encryption if the server relays traffic between clients, and only
the necessary ports, open in the machine's firewall and in the provider's. Self-contained
deployment, as a service that starts on its own, automated and with its credentials as secrets; logs
that rotate and an automatic check at the end of each deployment.

**Why.** A server is exposed to the whole internet: every extra open port is a door, and a server
that relays other people's content should not be able to read it.

## Annex D: native code

**What it says.** Native code (C++) goes in its own module with a minimal boundary to the rest; it is
built with a single script and the documented tools; it links against system functions instead of
redistributing third-party libraries with restrictive licenses; and it handles its resources and
errors explicitly, without passing silent failures on to the rest of the app.

**Why.** Native code is where one error can bring down the whole program: the smaller and clearer
its boundary, the easier it is to find.

## Annex E: shared components and design

### E.1 Custom dialogs

**What it says.** System dialogs are forbidden; a shared custom one is used instead (a rounded card
over a veil, with the app's theme and color) that replaces them one for one.

**Why.** The system ones break visual consistency and do not follow the theme.

### E.2 Author's notes

**What it says.** There is a floating button for taking notes with the context of the screen, only
on the author's devices and **only in development builds**: in the ones that are published it is
completely disabled, and this is checked before each release.

**Why.** It is a work tool that must never reach the people who use the app.

### E.3 System bars

**What it says.** Since Android 15, apps are drawn edge to edge, so the content is kept clear of the
status and navigation bars and the gap is painted with the brand color; never full screen.

**Why.** Otherwise, the system bars cover buttons and text.

### E.4 to E.8 Palette, icon, menu, signing, and splash screen

**What it says.** All apps share **exactly the same indigo palette**, with no accent of their own:
red only for destructive actions or errors and green only for positive ones. Each app's icon is a
white drawing on an indigo gradient, legible at small sizes. The menu header carries only the logo
and the name, with no taglines, and the menu footer shows the version. Navigation is a side menu,
never a bottom button bar. The signing password never goes in the repository. And the startup
screen is the system's native one, in indigo, with no artificial welcome screens that make people
wait for no reason.

**Why.** They are all recognized as part of the same family without redoing the work in each one;
and a welcome screen with a made-up wait only delays whoever wants to use the app.
