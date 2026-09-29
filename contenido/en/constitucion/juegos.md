# Games constitution
- slug: games
- documento: CONSTITUCION-GAMES.md
- orden: 4
- actualizado: 2026-09-23
- lema: A free engine, assets with proven licenses, no purchases or ads, and 60 frames per second.

Extends the general constitution for the catalog's video games.

## 1. Engine and structure

**What it says.** Games are made with a **free game engine** (MIT-licensed), with their scenes and
scripts stored in the repository. Every game has the same minimum structure: scenes, logic, assets
(art, audio, fonts), development tools, and translatable text. Development tools are **not
packaged** into the final game.

**Why.** A free engine meets the catalog's licensing rule; a fixed structure means anyone knows
where to look; and whatever is only useful for development has no reason to take up space on the
player's device.

## 2. Assets and licenses

### 2.1 Every asset, with a suitable license

**What it says.** Art, music, sound effects, fonts, and voices must be MIT-compatible or free for
commercial use, just like the code. No exceptions.

**Why.** A game is as much its assets as its code: an image with a license that doesn't allow it
would prevent sharing the game just as a library would.

### 2.2 Documented origin

**What it says.** Every asset has its origin and license written down. If they can't be proven, it
doesn't go in.

**Why.** "I found it on the internet" is not a license.

### 2.3 Generated voice and audio

**What it says.** Generated voices are made with voice engines whose license allows commercial use.
One that didn't allow it was ruled out.

**Why.** It's rule 1.1 of the general constitution applied to voice.

### 2.4 Generated assets, reproducible

**What it says.** Whatever a tool of the game itself produces can be generated again: the script
that produces it is stored alongside the result.

**Why.** If it needs changing, you change the script and regenerate, instead of hand-editing
something nobody knows how it was made.

## 3. Content

**What it says.** An appropriate age rating, declared in the store. No in-app purchases, no ads,
and no telemetry. Progress is saved **on the device**: a game doesn't need an account. If there were
ever shared games or leaderboards, the name the player enters would go out encrypted like any
other user text.

**Why.** A game is no exception to the idea of the catalog: free, no ads, and not measuring anyone.

## 4. Interface

**What it says.** The shared design (indigo palette, rounded corners, light and dark mode), buttons
with flat icons, and menus that work with a controller and a touchscreen, not just a mouse.

**Why.** People play in many ways, and a menu that only works with a mouse leaves out anyone
playing on a phone or with a controller.

## 5. Languages

**What it says.** Spanish and English are mandatory, with all text extracted into translation
files. No text written inside scenes or scripts.

**Why.** As in the rest of the catalog: translating should be a matter of filling in a table.

## 6. Performance

**What it says.** Target: **a steady 60 frames per second** on the reference device. There is a
maximum texture size set for each project and applied before exporting, and before publishing, the
loading time, memory, and smoothness are measured in the heaviest scene.

**Why.** What isn't measured gets worse without anyone noticing, and oversized textures are the
easiest way to make a game slow and heavy.

## 7. Publishing

**What it says.** If a game goes to Google Play, the mobile apps constitution applies to it too:
the same signing key, the same version format, the Android version Google requires, and a listing
with real screenshots of the game. The Android build is done with a script.

**Why.** To Google Play, a game is just another app, with the same rules.
