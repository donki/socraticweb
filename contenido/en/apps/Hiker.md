# Hiker
- slug: hiker
- plataformas: Android
- lema: Record your routes with GPS, snap them to the trails and follow them again.
- github: https://github.com/donki/Hiker
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.hiker — solo en la pista de prueba cerrada (alpha 2026091202 publicada; la 2026091902 sigue en borrador), sin producción; la página pública de Play aún no existe (devuelve 404 a 2026-09-25) (fuente: D:\sOCProjects\05-PENDIENTE-Hiker.md; paquete en Hiker.csproj y GooglePlayConsole\Hiker\ficha.md)
  - Microsoft Store: no publicada (solo Android; no hay ficha ni ID de Store en el proyecto)
- descarga_alternativa: https://github.com/donki/Hiker/releases (última: v2026.09.19.02, APK)
## Description
Hiker is your hiking companion: it records the route you walk on a full-screen map, saves it on your phone and helps you follow it next time, telling you how much is left and warning you if you stray from the trail.

Recording keeps going with the screen off and the phone in your pocket, and if Android closes the app in the middle of a long route, when you open it again it offers to recover what was recorded. When you finish, Hiker can snap your track to the paths on the map and pull it out of buildings, showing you both versions so you can choose which one to save.

For each route you get a detail sheet with distance, elevation gain and loss, altitudes, times, speeds and the elevation profile drawn out. You can import routes in GPX format. Your routes stay on your phone: no accounts, no ads, no trackers.

## Main features
- Full-screen map with your real-time position, accuracy and speed.
- Route recording that keeps going with the screen off, with a notification while recording.
- Recording recovery if Android closes the app mid-route.
- Snapping the route to the paths on the map, comparing the recorded and snapped versions on the map before saving.
- Following a saved route: distance to the track, what's left, and a red warning if you get more than 50 m away.
- Heading mode: the map rotates with the compass so that what's in front of you is at the top.
- Detail sheet for each route with distance, elevation gain and loss, altitudes, duration, moving time, pace, speeds and elevation profile.
- Importing routes in GPX format.
- In Spanish and English, with light and dark mode.

## User guide (support)

### Getting started
1. Open Hiker. Android will ask you for **location while using the app** permission: accept it with precise location, because that's what places your position on the map and records the route. The app doesn't need location "all the time": when you record, it does so with a visible notification.
2. When you start recording, Android may ask you for **notifications** permission: it's the "Recording the route" notification, which lets recording continue with the screen off.
3. The first time, Hiker asks you about **Battery Optimization** ("...allow the app to run without battery restrictions. Do you want to change this setting now?") and about **Background Execution**. Answer **Yes** and remove the restrictions in the settings that open: that way the system won't cut off recording on long routes. Each question appears only once.
4. Wait for the map to center on your position ("Getting location..."). Outdoors and after a few seconds, accuracy improves.

### Everyday use
- **Record**: tap the red record button on the map (or **Record** in the menu), walk, and when you finish tap **Stop**. Hiker asks whether you want to save the route, offers to snap it to the map and asks you for a name.
- **Follow a route**: in **Routes**, tap the route's location button; it's drawn on the map and the follow bar appears.
- **View a route**: in **Routes**, tap the information button to see its detail sheet.

### Side menu
- **GPS**: expands the map submenu. Next to each option there's an information button that explains what it does.
  - **Map**: shows the full-screen map without starting any recording.
  - **Record**: starts recording your track by logging GPS points.
  - **Stop**: stops the recording in progress.
  - **Follow: On / Follow: Off**: keeps (or stops keeping) the map automatically centered on your position.
  - **Heading: On / Heading: Off**: rotates the map so the direction you're facing points up. It's on by default.
  - **Save**: saves the recorded track as a named route.
  - **Clear**: removes the current track from the map without saving it.
- **Routes**: your saved routes.
- **Settings**: the language.
- **About**: version, contact, language, privacy, license and legal notice.
- The installed version appears at the bottom.

### Map screen (GPS)
- **Status header**: an icon with the status (stopped, recording) and your position: "Lat · Lon · ±accuracy in meters · speed in km/h".
- **Map**: move and zoom it with your fingers; your position appears as a dot and the recorded or loaded route as a line.
- **Location button**: re-centers the map on your current position.
- **Record button** (red): starts recording. While recording, the **Recording the route** bar appears with the time, distance and points logged, and the **Stop** button.
- **When you stop**:
  1. "Route recorded. N points recorded (X km). Do you want to save it?": **Save** or **Discard** (discarding removes it from the map).
  2. If you save, Hiker checks the paths on the map ("Snapping the route… Checking the paths on the map"). If there's no connection, it lets you know and saves the route as it was recorded; if it already fit, it tells you so and continues.
  3. If it has snapped it, you'll see both versions: in red the one that would be saved and in gray the other, with the text "In red: snapped route — N points snapped to paths and M pulled out of buildings" or "In red: recorded route". The **toggle** button (arrows) switches which one is in red and the **save** button (floppy disk) keeps the one in red.
  4. Finally, **Save Route** asks you for the **Route name** (**Save** / **Cancel**) and confirms "Route 'name' saved successfully".
- **Follow bar** (when you load a route from Routes): "Following the route" with the total length; on the move it shows "On the route: X from the track" and "X left", with a green dot, or "Off route: X from the route", with the dot in red, if you get more than 50 m away. The **Stop** button on the bar stops following it.
- **Interrupted recording**: if Android closed the app while you were recording, when you open it again you'll see "An unsaved recording with N points was left. Recover it?": **Recover** or **Discard**.

### Routes screen (Saved Routes)
- Each route shows its name, **Distance** in km and **Date**, with three buttons:
  - **Information**: opens the route's detail sheet.
  - **Location**: draws it on the map and starts following it.
  - **Trash**: deletes it after asking "Delete the route 'name'?".
- **Load GPX** (folder icon): choose a .gpx file on your phone and it's imported as a route ("Route 'name' imported."). If the file has no points, it lets you know.
- **Refresh** (arrows icon): reloads the list.

### Route detail screen
- Name and date of the route.
- **Distance**, **Elevation gain**, **Elevation loss**, **Max altitude**, **Min altitude**, **Altitude range**, **Duration**, **Moving time**, **Pace** (minutes per km), **Average speed**, **Max speed** and **Points**. Elevation gain and loss are smoothed so GPS noise isn't added up.
- **Elevation profile**: chart of altitude (m) along the distance covered (km). If the route has no altitude: "This route has no altitude data."
- **Show on map**: opens the route on the map to follow it.

### Settings screen
- **Language**: **Español** or **English** ("Select your preferred language"). It's saved only when you tap it, and the interface changes right away. When installed, it uses Spanish if the phone is in Spanish and English otherwise.
- There are no other settings: GPS configures itself.

### About screen
- Name, **Version** and author (Socratic).
- **Contact**: button with the email address; opens your email app.
- **Language**: **Español** / **English**.
- **Privacy**, **License** (MIT) and **Legal Notice** ("Use at your own risk").

## FAQ
**The route comes out in pieces or gets cut off with the screen off.**
Remove Hiker's battery and background restrictions (Android Settings › Apps › Hiker › Battery › Unrestricted; on Xiaomi, also "Autostart"). Keep notifications permission turned on: the "Recording the route" notification is what lets Android keep providing positions with the screen off.

**Android closed the app in the middle of the route. Have I lost what I recorded?**
No: each point is saved on the phone right away. When you open Hiker again you'll see "Recording interrupted" and you can tap **Recover**.

**The map doesn't center on my position or shows up somewhere else.**
Check that location is turned on on your phone and that Hiker has precise location permission. Wait a few seconds outdoors and tap the location button. In dense forests, canyons or among tall buildings the GPS signal is worse.

**When saving it says "Could not check the map".**
Snapping to paths needs a connection. Without one, the route is still saved as it was recorded.

**Snapping moved my route onto a path I didn't take.**
Before saving you can tap the toggle button to see the recorded route in red and save that one instead of the snapped one.

**Can I load routes made in another app or on the web?**
Yes, if they're in GPX format: in **Routes** tap **Load GPX** and choose the file. To create or edit routes on your computer you can use free web tools such as GPX Studio and then move the file to your phone.

**The map rotates by itself and makes me dizzy.**
That's Heading mode. Turn it off in the side menu › **GPS** › **Heading: Off**.

**The detail sheet says "This route has no altitude data".**
Some imported GPX files don't include the altitude of each point; without it, elevation gain and loss and the profile can't be calculated.

## Privacy
Your routes and your position are saved only on your phone; there are no accounts, ads or trackers, and Hiker doesn't send your tracks to any server. To draw the map, the map library and the OpenFreeMap tiles for the area you're viewing are downloaded and, only when snapping a route to paths, OpenStreetMap is asked which paths and buildings there are in the area it goes through (without saving anything there); in addition, at startup it checks whether there's a new version.
