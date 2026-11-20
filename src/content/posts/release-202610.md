---
title: "October 2026: formatted notes and the fleet map"
description: "Write notes with formatting everywhere, see where you have ridden on the new fleet map, and let the iOS app remember new fuel stations for you."
date: 2026-10-09
updated: 2026-10-21
versions:
  web: "2026.10.2"
  ios: "0.16.0"
---

October brings formatted notes to the web app and the iOS app, a map of everywhere your
motorcycles have been, and a smoother fuel log on the iPhone. This post covers web app
**2026.10.0 – 2026.10.2** and iOS app **0.14.0 – 0.16.0**.

## Highlights

### Formatted notes

Notes are no longer plain text. Maintenance entries, issues, expenses, parts, stock and
owners all take formatted notes — headings, lists, bold and links — written in an editor
that shows the result as you type. Torque specs get the same editor, so tightening
sequences and remarks stay readable. Both the web app and the iOS app support it.

### The fleet map

A new map page in the web app shows where your motorcycles have been: a heatmap of your
fill-ups, the legs between them, your tours and a year in review.

### Fuel stations remember themselves

When you log a fill-up in the iOS app and no saved station is nearby, the app now saves
the new station on its own — next time it is already there.

### Better feedback in the iOS app

Signing in with a wrong username or password now shows a clear message. Loading
placeholders stay until the first sync has finished, so lists no longer flash empty.
Outdated builds show an update prompt that stays until you update.

## Web app

### 2026.10.2 – October 21

- Maintenance and security updates; nothing visible changes.

[All changes](https://github.com/mightea/MotoManager/compare/2026.10.1...2026.10.2)

### 2026.10.1 – October 11

- New fleet map with a fuel heatmap, legs, tours and a year in review.
- Fix: statistics charts no longer stretch a single year across the whole card.
- Fix: the workshop table on the map page shows full dates and all visits.

[All changes](https://github.com/mightea/MotoManager/compare/2026.10.0...2026.10.1)

### 2026.10.0 – October 9

- Formatted notes for maintenance, issues, expenses, parts and owners.
- Formatted torque spec notes with an editor that shows the result as you type.

[All changes](https://github.com/mightea/MotoManager/compare/2026.9.3...2026.10.0)

## iOS app

### 0.16.0 – October 21

- Outdated builds show an update prompt that stays until you update.
- Fix: the fuel sheet drops the station checkmark and gets a larger clear button.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.15.0...v0.16.0)

### 0.15.0 – October 21

- A new fuel station is saved automatically when no nearby one matches.
- Fix: logging in with a wrong username or password shows an error.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.14.0...v0.15.0)

### 0.14.0 – October 9

- Formatted notes for maintenance, issues, parts and stock.
- Formatted torque spec notes with a rich text editor.
- Fix: loading placeholders stay up until the first sync has landed.
- Fix: the empty fuel log's button shows its plus icon again.
- Fix: buttons in empty lists no longer stretch into tall pillars.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.13.0...v0.14.0)
