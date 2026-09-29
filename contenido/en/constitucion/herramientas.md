# Windows tools constitution
- slug: tools
- documento: CONSTITUCION-TOOLS.md
- orden: 3
- actualizado: 2026-09-23
- lema: Internal and desktop utilities: they should do one thing, break nothing by default, and say what they did.

Extends the general constitution for tools: support programs, desktop utilities, and generators
used to build the rest of the catalog.

## 1. What a tool is

**What it says.** It is support software: automation scripts, desktop utilities, generators. It is
not published in stores and has no users outside the project. That relaxes the rules on store
listings and age ratings, but **not** those on licensing, security, or privacy.

**Why.** Being internal doesn't make something harmless: a tool usually has more access (accounts,
devices, publishing) than a regular app.

## 2. Rules

### 2.1 A tool does one thing

**What it says.** If it grows to the point of needing its own full interface and distribution, it
stops being a tool and is treated as an app.

**Why.** That way each one can be understood at a glance, and whatever turns into a product gets
the rules of a product.

### 2.2 Reproducible

**What it says.** It runs with a single command documented in its README, with its dependencies
declared.

**Why.** If only the person who wrote it knows how to use it, the day that person or that memory is
gone, it can't be used.

### 2.3 No destructive effects by default

**What it says.** Anything that deletes, overwrites, or publishes asks for confirmation or an
explicit option, and whenever it makes sense there is a dry-run mode that shows what it would do
without doing it.

**Why.** A mistake when running a tool should never be able to delete or publish anything that
wasn't asked for on purpose.

### 2.4 Idempotent

**What it says.** Whenever possible, running it twice doesn't leave things worse than running it
once.

**Why.** It can be run again without fear after a half-finished failure.

### 2.5 Readable output

**What it says.** When it finishes, it's clear what it did, what it skipped, and why.

**Why.** A tool that finishes silently doesn't let you know whether it worked.

### 2.6 Flat icons if it has a window

**What it says.** As across the whole catalog: single-color line drawings, never emoji.

**Why.** For the same reasons as in the general constitution (6.2).

## 3. Secrets

**What it says.** Secrets never go inside the code: they are read from a local file that is not
pushed to the repository. Tools that touch the Google Play Console, accounts, or devices state in
their README what they access. Any tool exposed to the network requires strong authentication
(token, per-request signature, rate limiting, and an allowlist), and without a token it responds
"unauthorized." And a tool that touches an app's database leaves **encrypted** whatever is
encrypted: no decrypting it to view it comfortably in a dump, a log, or a screenshot.

**Why.** Whatever gets decrypted "just to take a look" ends up in a file nobody deletes. If it needs
to be seen, it's seen from the app, which is the one that holds the key.

## 4. Dangerous automation

**What it says.** Tools that run commands on the computer or publish to stores have only the
permissions they need, log what they do, and don't skip security confirmations except by an
explicit, deliberate decision.

**Why.** They are the ones that can do the most damage with a mistake, so they are the ones watched
most closely.

## 5. Documentation

**What it says.** Every tool has a README covering what it does, how to run it, what it needs
installed, what it accesses, and what it can break.

**Why.** Before running something, you need to know what can happen.
