# Website constitution
- slug: web
- documento: CONSTITUCION-WEB.md
- orden: 5
- actualizado: 2026-09-29
- lema: This very website: no tracking, a single privacy policy, bilingual, and every app explained screen by screen.

Extends the general constitution for this website and for any of the project's internet services.

## 1. Principles

**What it says.** Six principles for any of the project's websites:

1. **No tracking**: no analytics, third-party cookies, tracking pixels, or fonts loaded from other
   sites.
2. **Static by default**: if it can be done with HTML and CSS, no JavaScript is added.
3. **Self-contained**: nothing loaded from other people's servers.
4. **Accessible**: meaningful HTML, enough contrast, and it works without JavaScript and with the
   keyboard.
5. **Responsive**: readable on a phone, with no horizontal scrolling.
6. **Light and dark mode**, following the system preference.

**Why.** Every piece loaded from another site tells that site who is visiting the website. Without
them, the website can be hosted anywhere and doesn't leak visits; and simple things work on more
devices and break less.

## 2. The privacy policy is part of the product

**What it says.**

- There is **a single** policy for all the apps, and its address is in the Google Play listing and
  on the "About" screen of each one. If the address changes, it has to be changed in all those
  places.
- It is written **generically, by case**: apps that run entirely on the device, and apps that sync
  and need an account and a server. Each one accesses only what it needs for the feature it
  advertises; the permission details go in its listing.
- **Exception**: an app that handles a different kind of data gets its own section. Today that's
  Family Together, which shares location within a group; its section says what is sent and how
  often, how it's encrypted, how long it's kept, how it's deleted, and which third parties receive
  it, by name, because the law requires it.
- The "syncs" case has its conditions in writing: an account the user already has, without seeing
  or storing passwords, content **encrypted on the device before it leaves**, only what the
  feature needs, and no advertising, profiling, or analytics.
- **The policy, the store listing, and the app say the same thing.** If what is stored, or where,
  changes, all three change in the same cycle, and the policy **before** anything is published.
- A copy of the policy is also on Google Sites, which is updated by hand.
- The date of its last update is shown in plain sight.

**Why.** Google rejects listings with a broken privacy policy. Writing it by case means a new app
doesn't force a rewrite. And publishing with a policy that doesn't match what the app does is
making a false statement: until September 1, 2026 it said there were no accounts or server, and
that was no longer true.

## 3. Where the website lives

**What it says.**

- The website is hosted on a website hosting service, on its free plan. **The source of truth is
  the repository**, never the host's editor: anything changed by hand there is lost on the next
  publish.
- Each app has its page in a text file with a fixed header (page name, platforms, tagline,
  repository, stores and their status) and always the same sections: description, features, user
  guide, frequently asked questions, and privacy.
- A generator produces at the same time a **local copy** that can be browsed without a server and
  the content exactly as it is published, and both are stored in the repository. Another command
  of the same generator publishes it. The publishing credential lives outside the repository.
- No plugins, third-party widgets, or tracking code. The host's own statistics come built into the
  free plan: that's the only exception to the no-tracking principle, and it affects only the
  hosted website, not the local copy.
- The design goes in each page's own blocks (colors, borders, grids that rearrange themselves on a
  phone), because the free plan doesn't allow custom style sheets.
- Before anything is considered finished, it's checked on desktop and on mobile, with screenshots
  of the published website: mobile with **device emulation**, not with a narrow window. Nothing
  may have horizontal scrolling.
- Comments are closed across the whole site, with no "Like" or share buttons.

**Why.** With the repository as the only source, the website can be regenerated in full or moved
to another host without losing anything. Mobile testing with emulation became a rule because a
narrow window won't shrink below a certain width and the screenshot comes out cut off, hiding
exactly the bugs you're looking for.

## 3 bis. Regulations (Spain and the European Union)

**What it says.** The website complies with the LSSI-CE (Spain's information society services
law), the General Data Protection Regulation (GDPR), and Spain's data protection law, with three
pages linked from the footer of every page:

- **Legal notice**: who the owner is, contact, purpose, intellectual property, links, liability,
  and applicable law. Today with a name and email; if the website had economic activity, a tax ID
  and address would have to be added.
- **Privacy**: the apps' policy plus the website's, with the rights and how to file a complaint
  with the Spanish Data Protection Agency (AEPD).
- **Cookies**: each cookie with who sets it, what for, and how long it lasts, and how to reject
  them, with a notice on every page.

There is a **known limitation**, written down as is: the host sets its statistics cookies on
arrival, before anything is accepted, and on the free plan this can't be prevented. Complying to
the letter would require a paid plan or self-hosting with the local copy. And when the cookies
change, they are measured again with the browser and the policy is updated.

**Why.** It's the law. And writing down the limitation instead of hiding it is the same honesty the
general constitution asks for with encryption (5.8).

## 4. Content

**What it says.** The website has a **home page** (what sOCratic is, the cards for all the apps,
and the idea of the catalog), **one page per app** (tagline, platforms, description, features,
privacy, screenshots, and download links), and **a support guide** per app (how to get started,
every screen with all its options, and frequently asked questions). Plus this **Constitution**
section. Its rules:

- **Every app in the catalog is on the website**, unless its repository is private or it's
  unfinished. Currently left out: sOC the Game (unfinished), a remote access project (private), and
  sOC Lucia (by choice).
- **With every change to any app, check whether the website needs updating**: its page, its guide,
  or the status of its stores. If something user-facing changes, its guide changes, since it
  describes the version you can download today.
- **Download**: the store if the app is actually published (in closed testing it has no public
  page, so it links to GitHub) and **always GitHub**, unless the repository is private.
- Screen and option names are copied from the app's real text, not made up.
- **In Spanish and in English**, with the same templates, menu, and footer; English lives under
  /en/, with screen names copied from the app in English. **A page that changes, changes in both
  languages in the same cycle.** The language is switched with the **flags** in the menu, drawn as
  images and never as emoji.
- **Images** of each app taken from its store listings, reduced and uploaded only once; if they
  change in the store, they change here.
- **The top menu stays fixed** when scrolling.
- **No email in sight**: support goes through GitHub issues, and the address only appears where the
  law requires it (legal notice and privacy).
- **The idea of the catalog, in the general texts**: the apps are free to use and ad-free, made to
  learn and to help others learn, with the source code open on GitHub. And it's **an experiment in
  spec-driven programming with AI**: first we write down what each app must do and the rules it
  follows (this constitution is the fixed part), and large language models (LLMs) write the code
  from that. They are referred to generically, **without naming any specific AI model or product**,
  and without any promise of a commercial product.
- **Proper names: only Microsoft's and Google's.** Other products and companies are described by
  what they are ("other browsers," "the maps service"...), except where the law or a license
  requires naming them (privacy, legal notice, attributions), and there only what is essential.
- **Buttons with flat icons**, as across the whole catalog.
- **The "Constitution" section** explains each document rule by rule, with a link to the full text
  and its date. **When the constitution changes, its page changes in the same cycle**, in both
  languages, and the generator warns if a document is newer than its explanation.

**Why.** The website is the front door to the catalog, and it's only useful if it tells the truth
as of today: a guide with a button that no longer exists, or a link to a store where the app isn't
available, does more harm than having no guide. Keeping email out of sight avoids spam, and GitHub
issues leave questions and their answers in view of everyone. The naming rule avoids trademark
problems and the like.

## 5. Server services

**What it says.** Today the only server is Task Manager's managed database service (and Family
Together's, in development), and although it isn't ours, the rules are the same or stricter:

- HTTPS required, secrets outside the repository, strong authentication, rate limiting, and
  logging.
- **Only the service's public key goes in the app**; the secret key and the admin key never
  appear in the code or in anything that is distributed.
- **Authorization is checked on the server**, with row-level rules that say who sees each row.
  The app not asking for something is not a protection.
- **User text, encrypted**, and if the server itself fills in any text field, that part is removed
  from it.
- **The database schema is stored as code**, in numbered files inside the app's repository, which
  are applied in order and can be rerun. No manual changes in the console that nobody later knows
  how to reproduce.
- **If the service goes down, the app keeps working** with the data on the device; what's lost is
  syncing.

**Why.** Anyone can read the code of a published app, so everything inside it is considered
public: a secret key in the client is a published key. That's why authorization lives on the
server, and the versioned schema makes it possible to rebuild the server from scratch.
