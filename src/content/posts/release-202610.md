---
title: "October 2026: a fleet map, formatted notes and smarter fuel stations"
description: "See where you rode on a fleet map with tours and a year in review, format your notes in both apps, and let the iPhone save new fuel stations for you."
date: 2026-10-09
updated: 2026-10-21
versions:
  web: "2026.10.2"
  ios: "0.16.0"
---

October is about looking back on the season and writing things down properly: a map of
everywhere your motorcycles took you, notes with formatting, and less tapping when you log
a fill-up on the iPhone. This post covers web app **2026.10.0 – 2026.10.2** and iOS app
**0.14.0 – 0.16.0**.

## Highlights

### Your season on a map

The web app has a new *Karte* page. It puts your fuel stops on a map as a heatmap, draws the
legs between consecutive stops in each motorcycle's colour, and lets you filter by
motorcycle and year. Below the map you find the numbers for the year — kilometres, litres,
fuel cost, riding days, tours, countries and your farthest point — plus a card for each
tour with a sketch of the route, a riding calendar and a table of your workshop visits.
Each year also gets its own year-in-review page, made to be shared as a screenshot, and
you can export your trips as GeoJSON. (Web app.)

### Formatted notes

Notes can now carry **bold**, *italic* and three highlight colours — red, yellow and blue — so the important
bit of a torque spec or a repair note stands out. It works for torque specs, maintenance
entries, defects, parts and stock notes in both apps; in the web app also for fuel entries,
expenses and previous-owner remarks. Notes stay readable as plain text wherever formatting
isn't shown.

### Fuel stations remember themselves

When you log a fill-up on the iPhone at a station MotoManager doesn't know yet, it is now
saved together with the fill-up — no extra tap on "Anlegen". The name stays editable until
you save, and a tap on the cross skips the station. Next time you fill up there, it is
recognised. (iOS app.)

### An update reminder that stays

When a newer version of the iOS app is needed, the reminder no longer disappears after a
few seconds. It stays on screen with a button that opens the update in TestFlight, or you
choose "Später". (iOS app.)

## Web app

### 2026.10.2 – October 21

- Maintenance and security updates; nothing visible changes.

[All changes](https://github.com/mightea/MotoManager/compare/2026.10.1...2026.10.2)

### 2026.10.1 – October 11

- A fleet map with a fuel-stop heatmap, the legs between stops, tours and a year in review.
- Fix: statistics charts no longer stretch a single year across the whole card.
- Fix: the workshop table on the map page shows full dates and every visit.

[All changes](https://github.com/mightea/MotoManager/compare/2026.10.0...2026.10.1)

### 2026.10.0 – October 9

- Formatted notes for torque specs, edited right in place.
- Formatted notes for maintenance and fuel entries, defects, expenses, parts, stock and previous owners.

[All changes](https://github.com/mightea/MotoManager/compare/2026.9.3...2026.10.0)

## iOS app

### 0.16.0 – October 21

- When an update is needed, the reminder stays on screen and opens the update in TestFlight.
- Fix: the fuel station field drops its checkmark and has a larger clear button.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.15.0...v0.16.0)

### 0.15.0 – October 21

- A fuel station that isn't known yet is saved automatically with the fill-up.
- Fix: logging in with a wrong username or password shows an error.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.14.0...v0.15.0)

### 0.14.0 – October 9

- Formatted notes for torque specs, maintenance entries, defects, parts and stock.
- Fix: a fresh install shows loading placeholders until your data has arrived, instead of briefly claiming there is nothing there.
- Fix: the button on the empty fuel list shows its plus icon.
- Fix: buttons in empty lists no longer stretch into a tall pillar.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.13.0...v0.14.0)
