# TDT Online
- slug: tdtonline
- plataformas: Android (phone and tablet), Android TV
- lema: Spanish free-to-air TV channels live, on your phone, tablet and TV.
- github: https://github.com/donki/TdtOnline
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.tdtonline — solo en la pista de prueba cerrada (alpha, versión 2026091301 publicada y 2026091302 en borrador); la página pública da 404 hasta que pase a producción, lo que exige antes 12 probadores durante 14 días (fuentes: D:\sOCProjects\07-PENDIENTE-TdtOnline.md, README.md; comprobado el 2026-09-25 que la URL pública devuelve 404). En Play figura como «TDT Online: TV en directo» (Mobile\GooglePlayConsole\TdtOnline\ficha.md).
  - Microsoft Store: no aplica (solo Android).
- descarga_alternativa: https://github.com/donki/TdtOnline/releases (APK; última: v2026.09.13.2)

## Description

TDT Online brings you the channels of Spanish digital terrestrial TV (TDT, Spain's free-to-air broadcast television) live over the internet, on your phone, your tablet and your Android TV. Open the app, pick a channel and watch it: no sign-ups, no accounts and no ads.

Channels are sorted into categories, with their logos, a search box and a favorites category to keep your usual ones close at hand. The TV guide shows you what's on now and what's coming up next on each channel, and the app remembers the last channel you watched so you can go back to it with one tap.

On the TV you can use it comfortably with the remote's D-pad, and on the phone with your finger. The app only opens the streams that each broadcaster publishes openly on the internet: it doesn't host or rebroadcast anything. That's why the channels you can only watch on their own sign-in platforms (such as Antena 3, laSexta, Telecinco or Cuatro) aren't there.

## Main features

- Spanish TDT channels live over the internet (RTVE, regional, themed and international channels) with their logos.
- Categories in tabs, with "Favorites" and "All" first.
- Channel search by name, ignoring accents and capitalization.
- Favorites with one tap on the star or by holding OK on the remote.
- TV guide: what each channel is showing now (with a progress bar) and what's next.
- The show on air on the player screen, with its time slot and description.
- "Last watched" to pick up what you were watching.
- If a stream fails, it automatically tries the channel's next available address.
- Your own channel lists (JSON or M3U/M3U8) in addition to the default list.
- Same interface on phone, tablet and Android TV; Spanish and English.

## User guide (support)

### Getting started

1. Install the app on your phone, tablet or Android TV (on the TV it shows up in the launcher with its own banner).
2. Open it: it doesn't ask for permissions, an account or any setup. It only needs an internet connection. On startup it downloads the channel list ("Loading channels…") and keeps a copy in case there's no network another day.
3. Tap a channel (or select it with the D-pad and press OK) to watch it.

### Everyday use

Choose a category in the top row, tap a channel and it opens full screen. Go back to return to the list; the focus returns to the channel you were watching. Mark your usual channels as favorites to always find them in the first category.

### Main screen

- **Header**: title, "N channels" counter and, if you've already watched one, **Last watched: <name>** (tap it to watch it again).
- Header buttons: **Settings** (gear), **TV guide** (grid) and **About** (i).
- **Search channel…**: filters all channels by name. With the remote, the keyboard's "Search" key closes it and moves the focus to the results. If nothing matches: "No channel matches …".
- **Categories**: **Favorites** (always visible; when empty, it explains how to fill it), **All** and one for each category in the list.
- **Channel grid**: logo, name, current show and favorite star. Tapping opens the channel; tapping the star or holding down the channel adds it to or removes it from favorites ("Added to favorites" / "Removed from favorites").
- Remote keys on Android TV: **Info** opens "About"; the **red button** opens the TV guide; **Menu** or **Refresh** downloads the list and the guide again.

### Player

- Full screen with the channel name, a **favorite** button and **Now: <show>** with its time slot and description.
- **Yellow button** on the remote: adds the channel to or removes it from favorites.
- If the main stream fails, "Trying another stream…" appears and the next one is tried; if none works, "This channel cannot be played right now".

### TV guide

One row per channel (favorites first) with the show currently on, its progress bar marked **Now**, and the ones that follow. The time is shown at the top. With the D-pad you move down channel by channel and across each row; OK on the channel or on a show opens the channel. While it's getting ready, "Loading the programme guide…"; if there's no data, "No programme guide available right now".

### Settings

- **Channel lists**: the lists the app uses. They're downloaded every time it starts; the first one sets the order of the categories and the others add channels and backup streams. tdt-canales JSON, TDTChannels JSON and M3U/M3U8 are accepted. The built-in one is labeled **default list**.
- Trash can on each list: removes it ("List removed").
- Address field (**https://…/list.m3u8**) and **+** button: adds a list ("List added"). It warns you if the address isn't valid or if the list is already there.
- **↻**: downloads the lists again right now.
- **↶**: restores the default list ("Default list restored").
- **Close**: goes back to the main screen.

### About

Version, description, **Contact**, **Language** (**Español** / **English**; applies right away), **Privacy**, **License**, **Legal notice** and **Close**.

## FAQ

**Why aren't Antena 3, laSexta, Telecinco, Cuatro and others there?** Those channels (and Neox, Nova, Mega, FDF, Energy, Divinity, Be Mad or Boing) don't publish their broadcast openly: you can only watch them on their own platforms, with sign-in and copy protection. The app can only offer open streams.

**I get "Could not load the channel list".** Check your internet connection and press refresh (on the TV, the Menu or Refresh button on the remote). If you've added your own lists and one of them doesn't download, you'll get a warning and the app carries on with the rest.

**A channel says "This channel cannot be played right now".** The broadcaster has cut or changed its internet stream. The app has already tried the backup addresses; try again later.

**Where's DMAX?** It only shows up when the channel has its live stream turned on on its website; right now it's off, so it doesn't appear.

**The TV guide is empty.** The guide takes a moment to load at startup ("Loading the programme guide…"). If it stays empty, the guide source isn't available at that moment.

**How do I add a favorite with the remote?** Hold OK on the channel, or press the yellow button while you're watching it.

**I changed the lists and my usual channels are gone.** In Settings, press **↶** to restore the default list.

## Privacy

TDT Online has no accounts, ads or analytics. It only downloads the channel list and the TV guide and opens each broadcaster's public streams; your favorites and the last channel you watched stay on your device.
