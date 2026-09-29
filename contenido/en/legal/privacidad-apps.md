*This is an English translation provided for convenience. In the event of any discrepancy, the Spanish version prevails.*

Last updated: September 29, 2026.

The sOCratic apps respect their users' privacy. This privacy policy explains how data is handled when you use them and applies to all apps published by sOCratic on Google Play.

## 1. Data collection

The sOCratic apps **do not collect data about you**: there are no profiles, no analytics, no advertising, no advertising IDs and no trackers. There are no exceptions to this.

Each app accesses only the data it needs for the function described in its Google Play listing, and for nothing else.

**Most apps work entirely on the device**: they do not require an account, they do not send anything off the device, and the data stays on the phone or with the Android system's own providers.

**Some apps offer to sync your content across several devices**, and that feature cannot exist without an account and a server. When an app does this, it says so in its Google Play listing and in the app itself, and the following always applies:

- You sign in with an account you **already have**. sOCratic does not create its own accounts and does not see, receive or store your password.
- The content you write **is encrypted on your device before it is sent** and is stored encrypted: it cannot be read on the server. The only data left unencrypted is what the server needs in order to work (dates, status flags and identifiers), which does not reveal what you have written.
- Only what that feature needs is stored, and only you (or the people you expressly share something with) can access it.
- There is still no advertising, profiling, analytics or tracking.

**One app, the family location app (Family Together), shares your location with the people in a closed group** that you create or join with the approval of a group admin. That is its purpose, and it explains it the first time you open it. In it, the following applies:

- There is no account or password: your user is an anonymous identifier created on the phone. If you want, you can link a Google or Microsoft account solely to recover your user on another phone; only that account's identifier is stored, never the password.
- Your position (latitude, longitude and accuracy), the time and the battery level are sent every time you move about 25 metres, even with the app closed; plus your display name, your avatar if you set one, the group's zones, the alerts you turn on and the SOS you send.
- Coordinates, names (yours, the groups' and the zones') and the avatar **are end-to-end encrypted** on the phone with a key that only the group's phones have: the server stores data it cannot read. Only dates, identifiers and the battery level stay unencrypted.
- Each group is closed: only its members see its data. You can pause sharing in each group, leave it and **delete your history** whenever you like from the app; location history is deleted automatically after 30 days.
- Drawing routes snapped to the streets is computed on the phone: the map service is only asked for fixed areas of the map, never the route.

Each app requests the minimum permissions needed for its function. Before you grant any permission, Android tells you which one it is and you decide whether to allow it; you can revoke it at any time from the system settings. Actions that affect the device, such as installing or uninstalling an app, are always confirmed by you in the system dialog.


## 2. Use of information

The data each app accesses is used exclusively for the functions that app describes in its Google Play listing, and for no other purpose. It is not used for advertising, for profiling or for automated decision-making.

The data resides on your device, under your control. Uninstalling an app deletes the data that app stores on the phone. Content that belongs to the Android system, such as SMS messages or your personal files, remains on the phone, and you can manage or delete it with the system's own tools.

In apps that work only on the device, sOCratic holds no data of yours that you could ask to have rectified or deleted. In apps that sync, you can view and modify your content from the app itself (which is where it is readable), delete it from there, and request by email the complete deletion of your account and everything associated with it.


## 3. Data sharing

sOCratic does not sell, transfer, rent or share personal or sensitive data with third parties, whether for advertising or for any other purpose. No data obtained through the permissions of these apps is transferred to third parties to facilitate a sale.

In apps that sync, the provider hosting the database acts solely as a service provider: it does not use your data for any purpose of its own and, moreover, the content it stores is encrypted.


## 4. Third-party services

Some apps check a public file in the project's GitHub repository at startup to let you know whether a newer version is available. That check does not send any of your data: it only downloads a public file containing the version number, and if there is no network connection the app works just the same.

The route-tracking app downloads map tiles from a public map provider. As with any web request, that provider receives the device's IP address and the map area requested, but it does not receive your routes or any personal data.

In the family location app, these third parties are involved:

- **Supabase** hosts the server and the database, in the European Union, and stores what is described in section 1, with the content encrypted.
- **Google (Firebase Cloud Messaging)** carries the notifications (SOS, zones and join requests). It receives a notification identifier for the device; messages only contain identifiers, never readable text or your position. No other Google or Firebase service is used.
- **OpenFreeMap** serves the map tiles: it receives the IP address and the map area being viewed, not your position or your data.
- **OpenStreetMap, through Overpass** (overpass-api.de, run by FOSSGIS e. V., Germany, and overpass.kumi.systems, run by Kumi Systems, Austria): to snap history routes to the streets, the phone asks for the street map of fixed squares of about 2 km. They receive the IP address and those squares, never the route, the times or who the person is. It can be turned off in the app's settings.
- **Google or Microsoft**, only if you link your account, verify who you are when you link or recover it.

In apps that sync, two further services are involved: the identity provider you choose to sign in with, which is the one that verifies who you are, and the provider that hosts the database. The app itself tells you which ones they are.

No app uses the Android advertising ID, analytics services, third-party tracking SDKs or advertising networks.


## 5. Security

Data that does not leave the device is protected by the Android system's own security and encryption mechanisms and by the screen lock you have set up.

Anything that is synced always travels over an encrypted connection and, in addition, the content you write is encrypted on the device itself before it leaves, so it cannot be read on the server.


## 6. Children's privacy

These apps do not knowingly collect personal information from children.


## 7. Changes to this policy

Any changes will be published on this same page, updating the last updated date shown at the top.


## 8. Contact

If you have any questions about this privacy policy, you can contact the developer at: jsoladelarosa@gmail.com

sOCratic — Privacy policy updated on September 29, 2026.
