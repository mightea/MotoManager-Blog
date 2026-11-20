---
name: motomanager-release-post
description: Write, update and publish the monthly MotoManager release-notes posts on blog.motomanager.org (repo mightea/MotoManager-Blog, an Astro site in MotoManager-Project/MotoManager-Blog). Use this whenever the user wants release notes, a "what's new" post, a monthly/December/etc. post, a patch release added to the blog, or asks to update or fix the blog — even if they just say "write the release notes for this month", "add 2026.12.3 to the blog" or "blog post for the new iOS version".
---

# MotoManager release post

The blog at **https://blog.motomanager.org** has one post per month, in the style of
Home Assistant's release posts: hand-written highlights first, then every release of
the month, with smaller updates added to that month's post as they ship. It covers
two components: the **web app** (`MotoManager`, CalVer like `2026.11.5`) and the
**iOS app** (`MotoManagerApp`, SemVer like `0.21.1`).

## Who reads it — this decides almost everything

The reader is a **rider using MotoManager**, not whoever runs the server and not a
developer. Write about what changes for them when they log a fill-up, check a service
interval or look for a part. So leave out, or reword so it doesn't show:

- **The API / backend** (`MotoManagerApi`): no API section, no endpoints, no API
  versions, no "update web app and API together" notes. Riders see API work only
  through the apps.
- **Server and admin matters**: the admin area, support mode, server statistics,
  server settings, entering or changing the server address, upgrade-requirement
  settings. Say "sync across your devices" rather than "sync with the server".
- **The "no prefilled server" change** (builds shipping without a default server URL)
  — never mention it, in highlights or release lists.
- **BMWBike** as a data source — say the missing details are "filled in for you".
- **Build, CI, App Store listing/screenshot tooling, dependency bumps, refactors,
  tests, docs.** If a release has nothing visible, write
  "Maintenance updates; nothing visible changes." (or "Maintenance and security
  updates; …") so the version list stays complete.
- **Changes reverted in the same period** (e.g. a layout added and removed again).

**Grey areas — describe what the rider sees, not how it's configured.** Some changes
start on the server or admin side but are visible to riders. Write about the visible part
only:

- An update prompt in the app is rider-facing ("the reminder stays on screen until you
  update"); the admin setting that triggers it is not.
- A fix for something that broke because of a server matter is written as what works
  again: iOS 0.21.1's changelog line "restore the server address for sessions that lost it"
  became "sessions that lost their connection settings in the previous update work again."
- Developer phrasing such as "load documents with a Bearer header instead of `?token=`
  URLs" becomes "documents open without your session appearing in the link."

**Write each month as it was.** If something changed later (the update prompt opened
TestFlight in October and the App Store from November), describe the month's version.
Later changes belong in later posts.

**Security section** only for protection a rider benefits from, such as sign-in, sessions
or their documents, in plain words. Patched dependencies and build-tool vulnerabilities
are covered by "Maintenance and security updates; nothing visible changes."

Language is English. Keep the app's German UI names where they are what the rider sees,
in italics: *Tanken*, *Technik*, *Wartung*, *Teile*, *KI-Zugriff*, *Voll getankt*, *Alle*.

## Workflow

### 1. Get fresh changelogs and collect the month

The raw material is each repo's release-please `CHANGELOG.md`. The clones sit next to
the blog in `MotoManager-Project/`: `MotoManager` (web app, GitHub `mightea/MotoManager`)
and `MotoManagerApp` (iOS app, GitHub `mightea/MotoManager-App`). Local clones can lag
behind GitHub, so pull first:

```sh
cd /Users/tobias/Developer/Private/MotoManager-Project
git -C MotoManager pull --ff-only && git -C MotoManagerApp pull --ff-only
python3 MotoManager-Blog/.claude/skills/motomanager-release-post/scripts/collect_changelog.py 2026-12
```

The script finds the clones two folders above the blog repo it lives in. If the blog is
somewhere else (a copy or a worktree), pass `--root <folder with the clones>`.

It prints every release of the month per component, newest first, as
`### <version> – <Month day>` with its compare URL. Each entry ends with its short commit
hash, and fixes are prefixed `Fix:`. The chore/CI/docs/test lines it skipped are listed
separately. If a pull fails (e.g. a dirty
working tree), don't touch the repo — read the changelog from GitHub instead
(`gh api repos/mightea/MotoManager/contents/CHANGELOG.md --jq .content | base64 -d`).

To understand what a terse entry means for the rider, read the commit
(`git -C MotoManager show <hash>`): the message body and the files it touches. That's how
you find out e.g. whether a "docs" change is actually text shown in the app. Details from
commit bodies and code are fair to use. Details you would have to guess are not.

### 2. New month or update?

Posts live at `src/content/posts/release-YYYYMM.md`. If the month's post exists, this is
an **update**. Read that post, then:

- Add the new `### <version> – <date>` sections at the top of each component's section.
- Bump `versions` and `updated` in the frontmatter.
- Update the version range in the intro's "This post covers …" sentence. It's easy to miss.
- Add a highlight only if the release has a rider-facing feature. Place it by importance,
  not at the end. If it's one of the month's headline features, add it to the
  `description` as well. Change the `title` only if the new feature beats one already
  named there.

Otherwise write a new post.

### 3. Write the post

For a new post, read the newest existing post first and match its voice. The shape:

```markdown
---
title: "December 2026: <two or three headline features>"
description: "<one sentence, rider benefits, ~25 words>"
date: 2026-12-03          # date of the month's first release
updated: 2026-12-18       # date of the newest release, once there is more than one
versions:
  web: "2026.12.4"        # newest version covered, per component
  ios: "0.23.0"
---

<2–3 sentence intro: what the month was about. Last sentence: "This post covers web app
**2026.12.0 – 2026.12.4** and iOS app **0.22.0 – 0.23.0**.">

## Highlights

### <Feature as a benefit, not a commit message>

<A short paragraph: what the rider can now do and why it helps. Say which app(s) have it
when it isn't both. Optional screenshot below the paragraph.>

## Security            <!-- only when there is something a rider would care about; plain words -->

## Web app

### 2026.12.4 – December 18

- <Rewritten entry, sentence case, ends with a full stop.>
- Fix: <what no longer goes wrong, from the rider's side.>

[All changes](<compare URL from the script>)

## iOS app

### 0.23.0 – December 18
...
```

Writing guidance:

- **Title**: "<Month YYYY>: " followed by two or three features, at most about 70
  characters in total. It shows up on index cards and in feeds.

- **Highlights**: 3–8, ordered by how much they matter to riders. Group related entries
  across both apps into one highlight (e.g. "Partial fill-ups" covered web, iOS and
  stats). Titles are benefits ("Fuel stations remember themselves"), not commit text.
- **Release entries**: rewrite every line for a rider — "Support replaced odometers with
  per-motorcycle odometer changes" becomes "Support replaced odometers with total and
  instrument readings." Merge near-duplicates (five "realign X with the design proposal"
  lines become one). Keep "Fix:" lines, phrased as what now works.
- Don't invent features or details the changelog and commits don't support. When unsure
  what something does for the rider, check the commit or leave it plain.
- Every release of the month gets a section, in date order newest first, each ending with
  its "All changes" compare link — including maintenance-only releases. Admin-only
  releases are the exception: skip the section, and let `versions` name the newest
  release you did include.

### 4. Screenshots (optional, period-accurate only)

Screenshots must show the UI as it was that month — a November screenshot in an August
post misleads. Sources:

- The App Store set: `MotoManagerApp/appstore/screenshots/de-DE/<DISPLAY_TYPE>/` (demo
  data, German UI). Older sets are in git history:
  `git -C MotoManagerApp log --format='%h %ad %s' --date=short -- appstore/screenshots`,
  then `git show <hash>:<path> > file.png`.
- Fresh simulator screenshots of the current app, when the post is about this month.

Look at each image before using it. Resize and save into `src/assets/YYYY-MM/`:

```sh
sips -s format jpeg -s formatOptions 80 --resampleWidth 640 in.png --out src/assets/2026-12/ios-x.jpg   # iPhone
sips -s format jpeg -s formatOptions 80 --resampleWidth 1400 in.png --out src/assets/2026-12/ipad-x.jpg # iPad
```

Reference them relatively under the highlight they illustrate, with descriptive alt text:
`![The parts tab on the iPhone: …](../../assets/2026-12/ios-parts.jpg)`. If there is no
period-accurate image, go without and say so in your reply.

### 5. Build, check, publish

```sh
cd /Users/tobias/Developer/Private/MotoManager-Project/MotoManager-Blog
pnpm install && pnpm build
grep -n -i 'api\b\|admin\|server\|bmwbike\|prefill\|token\|header' src/content/posts/release-YYYYMM.md   # audience check
```

Review the grep hits. Some are fine, for example "the login prefilled" via the QR code, or
the *KI-Zugriff* access tokens. Preview with
`pnpm preview` and look at the post in the browser — light and dark, and phone width.

Commit with a Conventional Commit message (e.g. `docs: add the December 2026 release
post`) and push. The repo belongs to the `mightea` GitHub account while `gh` normally runs
as the work account, and a plain `git push` picks up the wrong keychain credentials:

```sh
gh auth switch -u mightea
git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push
gh auth switch -u tobias-herrmann_nzzemu
```

Pushing to `main` deploys via `.github/workflows/deploy.yml`. Wait for the run
(`gh run watch <id> -R mightea/MotoManager-Blog`) and check the live URL
`https://blog.motomanager.org/YYYY/MM/release-YYYYMM/` returns 200.

## Site facts (for fixes beyond posts)

- Astro 5 with content collections; pages in `src/pages/`, layout `src/layouts/Base.astro`,
  styles `src/styles/global.css`.
- The design mirrors the web app's `MotoManager/app/app.css`: Dakar palette (Ultramarine
  `#1E5BFF`, Plum `#5B1D7A`, Sand `#E8A341`, Vermillion `#FF4124` — always four bands),
  Slate/Navy surfaces, Anton / IBM Plex Sans / JetBrains Mono, `.label-tag`, `.stamp`, the
  MM nameplate. Keep it in sync with the web app.
- Custom domain `blog.motomanager.org` (Cloudflare CNAME `blog` → `mightea.github.io`,
  DNS only, plus the GitHub verification TXT record); `public/CNAME` must stay.
