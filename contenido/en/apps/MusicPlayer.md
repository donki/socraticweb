# Music Player
- slug: musicplayer
- plataformas: Android / Android Auto
- lema: The music on your phone, by artist or composer, with playlists and in the car.
- github: https://github.com/donki/MusicPlayer
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.musicplayer — solo en la pista de prueba cerrada (alpha 2026091401), sin producción; la página pública de Play aún no existe (devuelve 404 a 2026-09-25) (fuente: D:\sOCProjects\04-PENDIENTE-MusicPlayer.md; paquete en MusicPlayer.csproj y README.md)
  - Microsoft Store: no publicada (solo Android; no hay ficha ni ID de Store en el proyecto)
- descarga_alternativa: https://github.com/donki/MusicPlayer/releases
## Description
Music Player plays the music you already have stored on your phone, with no accounts, no ads and no subscriptions: just your library. It sorts it by artist (or by composer, if you listen to classical music), lets you search instantly and make your own playlists, including a favorites one.

It keeps playing with the screen off, with the controls in the notification, and it works in Android Auto: in the car you have your whole library organized into artists, playlists and songs, with the steering-wheel buttons and by voice.

If you want, it can look up a photo and a short bio of each artist on Wikipedia; it's off by default and, when you turn it on, the only thing that leaves your phone is the artist's name. It also shows the song's lyrics when the file itself includes them, and even highlights the line that's playing.

## Main features
- Plays the audio formats Android supports: MP3, AAC/M4A, FLAC, OGG, Opus, WAV, MIDI and AMR.
- Library grouped by artist or by composer, with search by artist, song or album.
- Your own playlists and a Favorites playlist; a song can be added to several playlists at once.
- Shuffle and repeat for the playlist or a single song.
- Multiple selection to play, add to playlists, remove or delete several songs at once.
- Fixing song info (title, artist, album, composer, year, track) and custom picture.
- Song details with the lyrics, synced with the music when the file allows it.
- Artist photos and bios (optional, off by default).
- Android Auto with Favorites, Artists, Playlists and Songs folders, favorite, shuffle and repeat buttons, and voice control.
- When you open it again, it brings back the last song you were listening to, paused.

## User guide (support)

### Getting started
1. Open the app. In **Library** you'll see the **Access to your music** notice: "Music Player needs permission to read the audio files stored on this device. Nothing is uploaded anywhere." Tap **Grant access** and accept the Android permission. Without it there's nothing to play.
2. Android will also ask you for permission to **show notifications**: it's the notification with the playback controls, which lets the music keep playing with the screen off.
3. The app scans your phone ("Scanning the device…") and shows you the summary "N songs · N artists".
4. If it doesn't find anything ("No music found"), copy audio files to your phone and scan again. If your music is on a card or doesn't show up, use **Settings › Search the whole phone**.
5. Optional: if you want artist photos and bios, turn on **Settings › Look up artist photos and biographies**.

### Everyday use
- In **Library**, pick an artist, a song or a playlist and tap a song to start playing it.
- Control playback from the mini player at the bottom, from **Now playing**, from the notification or from the car.
- For any action on a song, tap its menu button (the three dots); for several at once, press and hold one to enter multiple selection.

### Side menu
- **Library**: artists, songs and playlists.
- **Now playing**: the song that's playing, full screen.
- **Settings**: library, online information, Android Auto and language.
- **About**: version, contact, language, privacy, license and legal notice.
- The installed version appears at the bottom.

### Library screen
- **Scan the device again** (arrows icon, top right): reads the music on your phone again.
- **Search box** ("Search artist, song or album"): filters instantly. If there are no matches: "Nothing matches".
- **Tabs** (with icon): **Artists**, **Songs** and **Playlists**.
- **Artists**: each artist (or composer) with their photo or the cover of their first song and the number of songs. Tap it to open the artist screen.
- **Songs**: all the songs. Tap one to play it; its menu button opens the song actions.
- **Playlists**: the **Favorites** playlist (always first; it can't be renamed or deleted) and your playlists. Tap one to open it. Each playlist's menu offers **Rename playlist** and **Delete** ("… will be deleted. The songs stay on the device."). The **New playlist** button asks for the **Playlist name** ("My playlist"); it warns you if one with that name already exists. If there aren't any: "No playlists yet".
- **Mini player** at the bottom: cover, title, artist, progress bar and previous / play-pause / next buttons. Tap it to open **Now playing**.

### Song menu (three-dot button)
- **Play**.
- **Add to favorites** / **Remove from favorites**.
- **Add to playlists**: opens the screen to tick several playlists at once.
- **Go to artist**.
- **Song details and lyrics**: opens the song details.
- **Edit song info**: opens the editing screen.
- **Remove from this playlist** (only inside a playlist).
- **Delete from device**: deletes the file ("This cannot be undone"), with Android's confirmation. The song also disappears from all playlists.

### Multiple selection
Press and hold a song in Songs, in an artist or in a playlist. A bar appears with the count ("N selected") and the buttons:
- **Play** the selection.
- **Add to playlists**.
- **Select all**.
- **More**: **Remove from this playlist** (inside a playlist) and **Delete from device** (a single confirmation for all of them).
- **Close**: leaves selection mode.

### Artist screen
- Artist photo, name and number of songs.
- Artist **bio** (if online lookup is turned on), trimmed to three lines with a three-dot button to see it in full or collapse it, and the source: "Image and text: Wikipedia / Wikidata (CC BY-SA), artist matched with MusicBrainz."
- If lookup is off, a notice with the **Turn on online lookup** button.
- **Refresh info** (arrows icon): looks up the photo and the bio again ("Info updated" or "Nothing found for this group").
- **Picture** (picture icon): changes the artist's photo: **From this device**, **From a web address** (you paste the address of an image), **Search it on Google** or **Remove the custom one**.
- **Rename group** (pencil icon): changes the artist's name in all their songs.
- **Play all** and **Shuffle**.
- List of the artist's songs, with their menu and multiple selection.

### Playlist screen
- Playlist name and number of songs.
- **Play all** and **Shuffle** (disabled if it's empty: "This playlist has no songs yet.").
- Songs with their menu (including **Remove from this playlist**) and multiple selection.

### Now playing screen
- Cover, title, artist, album and position in the queue ("3 of 12").
- Progress bar you can drag, with the elapsed time and the length.
- **Previous** (if the song has been playing for more than 3 seconds, it goes back to its start), **Play/Pause** and **Next**.
- **Favorite** (heart), **Shuffle** ("Shuffle on/off") and **Repeat**, which cycles through **Repeat off**, **Repeat all** and **Repeat one**.
- **Information**: opens the details and lyrics.
- **Add to playlists** and **Delete** (deletes the song from the device).
- If nothing is playing: "Nothing is playing. Pick a song from your library to start.", with a button to go to the **Library**.

### Song details screen
- Cover, title, artist, album, track data (**File**, **Length**...).
- **About the artist**: photo and bio (if online lookup is turned on).
- **Lyrics**: the ones included in the file itself or in an .lrc file with the same name next to it. If they're synced, **Follows the music** appears and the line that's playing gets highlighted. If there are none: "This song carries no lyrics... it never downloads them."
- Icon buttons to **edit** the info (pencil) and **close** the details (X).

### Song info screen (editing)
- Fields **Title** (required), **Artist**, **Album artist**, **Album**, **Composer**, **Track** and **Year**.
- **Picture**: the same choice as for the artist (from this device, from a web address, search it on Google or remove the custom one).
- **Look up info online**: looks up the song and, if it finds it, suggests the data (**Use it** fills in the fields for you to check and save). It needs online lookup turned on.
- **Undo the correction**: goes back to the file's data.
- **Save** and **Cancel**.
- The correction is saved by the app and, if the system allows it, also in Android's media index; the audio file is never rewritten.

### Add to playlists screen
- Tick all the playlists you want to add the song (or the selected songs) to.
- **New playlist** to create one on the spot.
- **Save** ("Added to N playlists") or **Cancel**.

### Settings screen
**Library**
- **Scan the device again**: reads the audio files the system has indexed. Use it after copying new music.
- **Search the whole phone**: asks the system to re-index the internal storage and every card, and adds what it finds ("N new songs"). It can take a few minutes.
- **Include all audio** (switch): also shows what the system doesn't flag as music, such as recordings, podcasts and audiobooks 30 seconds or longer.
- **Find covers**: for each song without a cover, takes the picture embedded in the file or the cover.jpg in its folder ("Covers found: N").
- **Re-read tags**: reads title, artist, album, composer, year and track from the files again and fills in what's missing, respecting what you've fixed by hand ("Songs completed: N").
- While it works, it shows the progress ("N of M…"); if a scan is already running, it lets you know.
- **Group by composer** (switch): groups by composer instead of by performer. Useful for classical music.

**Online information**
- **Look up artist photos and biographies** (switch, off by default): when you turn it on, only the artist's name is sent to MusicBrainz and Wikidata/Wikipedia to look up a photo and a short bio.
- **Delete downloaded images**: clears the saved photos ("Downloaded images deleted").

**Android Auto**
- Information only: the library is available in the car without setting anything up.

**Language**
- **Español** / **English**: the language applies right away.

### About screen
- Name, **Version** and author (Socratic), with the app's description.
- **Contact**: button to send an email ("Questions, bugs and ideas are welcome.").
- **Language**: **Español** / **English**.
- **Privacy**, **License** (MIT) and **Legal notice** ("Use at your own risk").

### Android Auto
- Connect your phone to the car and open Music Player from the list of media apps. You'll see **Favorites**, **Artists**, **Playlists** and **Songs**.
- On the car's playback screen you have, besides previous / pause / next, the **Favorite**, **Shuffle** and **Repeat** buttons; when they're on, the icon sits inside a filled circle.
- You can ask for music by voice with the car's assistant.

### New version notice
At startup, if there's a newer version, **Update available** appears ("Version X is available. You have Y. Do you want to open the download page?"): **Open** or **Later**.

## FAQ
**In the car it says "Open Music Player on the phone and allow access to your music."**
You haven't granted access to your music yet. Open the app on your phone (or tap **Open on the phone** in the car) and grant access; the car's library fills in by itself right away.

**Music Player doesn't show up in Android Auto.**
If you installed the app from a file and not from Google Play, Android Auto hides it: turn on Android Auto's developer settings and check "Unknown sources".

**It doesn't find my music or some songs are missing.**
Tap **Scan the device again** and, if they're still missing (for example, music on the card), **Settings › Search the whole phone**. If they're recordings, podcasts or audiobooks, turn on **Include all audio**.

**My songs show up as "Unknown artist" or "Untitled", or badly grouped.**
Use **Settings › Re-read tags** to fill in what's missing from the files. For a specific song, **Edit song info** from its menu; for a whole artist, **Rename group** on their screen.

**Covers don't show up.**
Tap **Settings › Find covers**: it uses the picture embedded in the file or the cover.jpg in its folder. You can also set a picture by hand from **Edit song info › Picture**.

**I can't see the artist photos or bios.**
Online lookup is off by default. Turn it on in **Settings › Look up artist photos and biographies** (it needs a connection). If an artist doesn't show up, tap **Refresh info** on their screen.

**The lyrics don't show up.**
Music Player doesn't download lyrics: it only shows the ones included in the file itself or in an .lrc file with the same name in the same folder.

**I deleted a song by mistake.**
"Delete from device" deletes the file from your phone and can't be undone. If you only wanted to take it out of a playlist, use **Remove from this playlist**.

## Privacy
Your music, your playlists and your preferences stay on your phone: no accounts, no ads, no analytics. There are only two internet connections: the check for a new version at startup and, only if you turn it on, the lookup of artist photos and bios, which sends only the artist's name to MusicBrainz, Wikidata and Wikipedia. If you also tap **Look up info online** when editing a song, its title and artist are looked up on MusicBrainz.
