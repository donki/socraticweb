# QuitSmoke
- slug: quitsmoke
- plataformas: Android
- lema: Cut down on smoking little by little: space out your cigarettes and save money.
- github: https://github.com/donki/QuitSmoke
- tiendas:
  - Google Play (prueba cerrada): https://play.google.com/store/apps/details?id=com.socratic.quitsmoke — solo en la pista de prueba cerrada, sin producción; la página pública de Play aún no existe (devuelve 404 a 2026-09-25) (fuente: D:\sOCProjects\03-PENDIENTE-QuitSmoke.md; paquete en QuitSmoke.csproj y GooglePlayConsole\QuitSmoke\ficha.md)
  - Microsoft Store: no publicada (solo Android; no hay ficha ni ID de Store en el proyecto)
- descarga_alternativa: https://github.com/donki/QuitSmoke/releases

## Description
QuitSmoke helps you smoke less gradually and realistically, at your own pace. Instead of asking you to quit cold turkey, it sets a maximum number of cigarettes per day and spreads that maximum across your waking hours, so you always know how many you have left and when the next one is due.

You log each cigarette with a single tap, even from the notification without opening the app, and QuitSmoke keeps track: how many you've had today, how long you've gone without smoking, how much you've spent and how much you've saved compared with your maximum. When you feel ready, you lower your maximum by one cigarette and keep making progress.

Everything stays on your phone: no accounts, no ads, no trackers. It's free software under the MIT license, made by sOCratic. QuitSmoke is a support tool and is not a substitute for advice from a healthcare professional.

## Main features
- Adjustable daily maximum of cigarettes and a button to lower it one at a time as you make progress.
- Automatic calculation of how long to wait between cigarettes based on your waking hours.
- Home screen with today's progress, your last cigarette, the next recommended one and your smoke-free time.
- Persistent notification with today's count, the time of your next cigarette and a "Smoke" button to log it without opening the app.
- Double confirmation when you're about to go over your daily limit.
- History of the last 30 days: total cigarettes, days recorded, daily average and reduction achieved.
- Money statistics: total spent, total saved, average spending per day and savings percentage, in 14 currencies.
- Health and motivation tips that change every time, in Spanish or English.
- Settings that save automatically.

## User guide (support)

### Getting started
1. Install the app and open it. Right after it starts, Android asks for permission to **show notifications**: allow it, because that's what lets you see today's count in the notification bar and log cigarettes from there with the "Smoke" button.
2. Open the side menu (the three lines at the top left) and go to **Settings**.
3. Set your **Maximum cigarettes per day** (what you smoke right now is a good starting point).
4. Adjust your **Waking hours**: the time you get up and the time you go to bed. With that and your maximum, the app works out the time between cigarettes.
5. Fill in the **Price Settings** (pack price, cigarettes per pack and currency) so the money figures come out right.
6. If your phone closes apps in the background (Xiaomi, Huawei, Samsung with aggressive battery saving...), tap **Configure All Permissions** so the notification doesn't disappear.

There's no save button to tap: every setting is saved as soon as you change it.

### Everyday use
- Every time you smoke, tap **Smoke Cigarette** on the home screen or **Smoke** in the notification.
- Check the home screen or the notification to see when the next one is due, and try to wait until then.
- Every now and then, look at **History** to see your reduction and the money you've saved.
- When you're comfortable with your maximum, go to Settings and tap **Reduce Maximum (gradual progress)**.

### Side menu
- **Home**: start screen with today's status.
- **History**: statistics for the last 30 days.
- **Settings**: daily maximum, schedule, prices and system permissions.
- **About**: version, contact, language, privacy, license and legal notice.
- The installed version appears at the bottom of the menu.

### Home screen
- **Tip of the day**: a randomly chosen health or motivation tip, labeled **Smart Tip**. It changes every time you open the screen or refresh.
- **Today's progress**: progress bar with **Smoked: X/Y** (how many you've had today versus your maximum) and **Remaining**.
- **Last**: time of the last cigarette you logged.
- **Next**: recommended time for the next one. If you haven't smoked yet today, it's the time you get up; if you've already reached your maximum, it shows "--".
- **Smoke-free**: time since your last cigarette.
- **Smoke Cigarette**: logs a cigarette at the current time and shows "Cigarette registered successfully". If you've already reached your maximum, the button changes to **Limit reached**; when you tap it, it asks "You have already smoked N cigarettes today. Do you want to continue?" (**Yes, smoke** / **No, wait**) and then asks for a **Final confirmation** ("Are you sure? This will exceed your daily limit.", **Yes, I'm sure** / **Cancel**). It's only logged if you confirm both times.
- **Refresh data**: reloads the data and shows another tip.
- **Today's statistics**: **Between cigarettes** (recommended time between one and the next) and **Awake hours** (based on your waking hours).
- While the app is open, the screen doesn't turn off by itself.

### Notification
- Title **"QuitSmoke: X/Y today"** with today's cigarettes versus your maximum.
- Text **"Next: HH:MM"**, **"Next: now"** if you can smoke already, or **"Daily limit reached"**.
- **Smoke** button: logs a cigarette without opening the app and updates the notification instantly.

### History screen
It shows "Loading history..." while it calculates, and then:
- **General Statistics** (last 30 days):
  - **Total cigarettes**: cigarettes logged.
  - **Days recorded**: days on which you smoked at least one.
  - **Average/day**: average number of cigarettes on those days.
  - **Reduction achieved**: the percentage you've smoked below your maximum, with a summary like "Reduction achieved: X% (smoked/planned cigarettes in N days)".
- **Economic Statistics**:
  - **Total spent**: what the cigarettes you smoked have cost you.
  - **Total saved**: what you haven't spent compared with smoking your maximum every day.
  - **Average/day**: average daily spending.
  - **% savings**: what you've saved relative to what you've spent.
- **Refresh data**: recalculates the statistics.

### Settings screen
Header "Settings — Preferences and permissions". Everything saves automatically when you change it.

**Status cards**
- **Battery saver**: shows whether the app is **Excluded from saver** or **Optimized (excluding recommended)**. It shows "Unverified" until you tap "Check Permission Status".
- **Autostart**: autostart status. Since Android doesn't allow apps to check it, after checking it shows "Check in system settings".

**Permission Settings**
- **Check Permission Status**: updates the two status cards.
- **Configure All Permissions**: asks to exclude the app from battery saving (or opens that system screen) and also opens the manufacturer's autostart and background activity settings. When it's done, it tells you: "System settings opened. Configure battery, autostart and background."
- **Battery**: only the battery saver exclusion.
- **Autostart**: opens the manufacturer's autostart settings.
- Notice: "For optimal operation, configure all permissions for background execution."

**Maximum cigarettes per day**
- **−** and **+** buttons on either side of the number, or type the number directly (minimum 1).
- Below it, **Time between cigarettes**: the resulting recommended interval (awake hours divided by the maximum).

**Waking hours**
- **Wake-up time**: 07:00 by default.
- **Sleep time**: 23:00 by default. It can be after midnight.

**Price Settings**
- **Pack price**: 5.00 by default.
- **Cigarettes per pack**: 20 by default.
- **Currency**: Euro, US Dollar, Pound Sterling, Japanese Yen, Canadian Dollar, Australian Dollar, Swiss Franc, Chinese Yuan, Mexican Peso, Argentine Peso, Chilean Peso, Colombian Peso, Peruvian Sol and Brazilian Real.
- Below it, **Price per cigarette**: the cost of each cigarette, calculated from the above.

**Reduce Maximum (gradual progress)**
- Lowers your daily maximum by one cigarette (never below 1) and saves it. This is the button you use to move forward with your plan.

### About screen
- Name, installed **Version** and author (Socratic).
- **Contact**: button with the email address; tapping it opens your email app with a "Contact from QuitSmoke" message. If you don't have one, it says "Email client not available on this device".
- **Language**: **Español** and **English** buttons; the interface, the tips and the notification change right away ("Language updated"). On install, the app uses Spanish if your phone is in Spanish and English otherwise.
- **Privacy**, **License** (MIT) and **Legal Notice** ("Use at your own risk").

### New version notice
When you open the home screen, if there's a newer version you'll see **Update available** ("A newer version is available (X). You have Y. Do you want to update?"). **Update** opens the downloads page; **Not now** closes it.

## FAQ
**I don't get the notification with the "Smoke" button.**
Make sure you granted notification permission (Android Settings › Apps › QuitSmoke › Notifications). The notification appears when you open the app and updates every time you log a cigarette.

**The notification disappears or doesn't update when my phone is locked.**
Some manufacturers close apps in the background. In Settings, tap **Configure All Permissions**, exclude QuitSmoke from battery saving and turn on autostart; then tap **Check Permission Status** to confirm.

**I've reached my limit and the button says "Limit reached". Can't I log any more?**
Yes, you can: tap the button and confirm twice. It's logged just the same, because what matters is that the count is accurate; the double question is only there to make you think about it.

**I changed a setting and I can't see a save button.**
You don't need one: settings save automatically as soon as you change each field or selector.

**The time between cigarettes looks odd.**
It's calculated by dividing your awake hours (from wake-up time to sleep time) by your daily maximum. Check your Waking hours in Settings.

**The money saved shows zero.**
Savings are measured against smoking your maximum every day; if you smoke exactly your maximum, there are no savings. Also check that the pack price and cigarettes per pack are set correctly.

**The app is in English.**
If your phone isn't set to Spanish, the app starts in English. Change it in **About › Language › Español**.

**The screen doesn't turn off while I'm using it.**
That's intentional while QuitSmoke is in the foreground; it turns off normally once you leave the app.

## Privacy
QuitSmoke stores your cigarette log, your schedule and your prices only on your phone; there are no accounts, ads or trackers, and none of that leaves your device. The only internet connection is a check for a new version when you open the app, and it doesn't send any of your data.
