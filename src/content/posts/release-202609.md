---
title: "September 2026: AI assistants, invoice import and BMW part numbers"
description: "Connect an AI assistant to your garage, import invoices from scans and photos, look up BMW part numbers — and a reworked workshop tab on the iPhone."
date: 2026-09-02
updated: 2026-09-28
versions:
  web: "2026.9.3"
  ios: "0.13.0"
---

September is about getting data into MotoManager with less typing — from AI assistants,
scanned invoices, shop order confirmations and BMW's parts catalogue — and about a calmer
iPhone app. This post covers web app **2026.9.0 – 2026.9.3** and iOS app
**0.10.0 – 0.13.0**.

## Highlights

### Connect an AI assistant (KI-Zugriff)

You can now connect an AI assistant such as Claude to your MotoManager data. Under
*KI-Zugriff* in the settings you create and revoke access tokens, and assistants that
connect through a sign-in show a consent page first, so you decide what gets access.
The iOS app lists your tokens too and marks the ones created through a connected
assistant. The *KI-Zugriff* page also walks you through the setup for Claude Desktop, claude.ai and the
Claude app.

### Import invoices from scans and photos

Drop a scan or a photo of a workshop invoice into the web app and MotoManager reads it
for you. Order confirmations from boxxerparts.de can be imported as well, with
suggestions for which of your motorcycles each part fits.

### BMW part numbers

Link a part to its BMW part number and MotoManager fills in the
missing details for you. Works in the web app and the iOS app.

### A calmer iPhone app

The workshop tab is now a single overview with readable torque specs. Every form opens
in the same full-height sheet, the motorcycle header shrinks as you scroll, and the
iPhone app stays in portrait. Layouts adapt better across iPhone and iPad.

## Web app

### 2026.9.3 – September 28

- Import invoices from raw scans and photos.
- Link parts to a BMW part number and have the missing details filled in.
- Fix: the oil type on maintenance entries is saved.

[All changes](https://github.com/mightea/MotoManager/compare/2026.9.2...2026.9.3)

### 2026.9.2 – September 24

- Import boxxerparts.de order confirmations with fitment suggestions.

[All changes](https://github.com/mightea/MotoManager/compare/2026.9.1...2026.9.2)

### 2026.9.1 – September 3

- The *KI-Zugriff* page explains how to connect Claude Desktop, claude.ai and the Claude app.

[All changes](https://github.com/mightea/MotoManager/compare/2026.9.0...2026.9.1)

### 2026.9.0 – September 2

- New *KI-Zugriff* settings page to manage access tokens for AI assistants.
- Consent page for assistants that connect through a sign-in.
- Security updates.

[All changes](https://github.com/mightea/MotoManager/compare/2026.8.5...2026.9.0)

## iOS app

### 0.13.0 – September 28

- Link parts to a BMW part number and have the missing details filled in.
- The workshop tab is one overview with readable torque specs.
- All forms use the same sheet, and every sheet opens at full height.
- The iPhone app stays in portrait.
- Fix: torque badges wrap instead of being squeezed.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.12.0...v0.13.0)

### 0.12.0 – September 24

- The motorcycle header shrinks as you scroll; on the iPhone, details open full screen.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.11.0...v0.12.0)

### 0.11.0 – September 21

- Motorcycle screens adapt better across iPhone and iPad.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.10.0...v0.11.0)

### 0.10.0 – September 3

- Manage AI assistant access tokens from the settings (*KI-Zugriff*).
- Tokens created through a connected assistant are marked as such.

[All changes](https://github.com/mightea/MotoManager-App/compare/v0.9.0...v0.10.0)
