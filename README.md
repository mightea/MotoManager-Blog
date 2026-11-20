# MotoManager Releases

Release notes blog for the MotoManager web app (`MotoManager`) and iOS app
(`MotoManagerApp`), written for the people who use them. Static Astro site, deployed
to GitHub Pages by `.github/workflows/deploy.yml` on every push to `main`.

## Writing

- **One post per month**: `src/content/posts/release-YYYYMM.md`, published at
  `/YYYY/MM/release-YYYYMM/`. Frontmatter: `title`, `description`, `date`,
  optional `updated`, `versions: { web, ios }` (newest version covered),
  optional `draft: true`.
- Structure: Highlights (hand-written) → Security → `## Web app` and
  `## iOS app` with a `### <version> – <Month day>` section per release.
- The audience is the rider using the app: describe what changes for them.
  No API section, endpoints or server/admin notes.
- **Screenshots** go in `src/assets/YYYY-MM/` and are referenced relatively
  from the post (`![alt](../../assets/2026-11/x.jpg)`). Resize them first,
  e.g. `sips -s format jpeg -s formatOptions 80 --resampleWidth 640 in.png --out out.jpg`
  (iPhone) or `--resampleWidth 1400` (iPad). The App Store set in
  `MotoManagerApp/appstore/screenshots/de-DE/` is a good source.
- **Patch release**: add a `### <version> – <date>` section at the top of the
  component's section, bump `versions` and `updated`.
- The raw material is each repo's release-please `CHANGELOG.md`. Rewrite the
  lines for users; leave out `ci`, `docs`, `chore` and `test`.

## Local

```sh
pnpm install
pnpm dev        # http://localhost:4321
pnpm build      # dist/
```

## Design

`src/styles/global.css` mirrors the web app (`MotoManager/app/app.css`): the
Dakar palette (Ultramarine · Plum · Sand · Vermillion, always four bands),
Slate/Navy surfaces, Anton / IBM Plex Sans / JetBrains Mono, `.label-tag`,
`.stamp` and the MM nameplate. Keep them in sync when the web app changes.

## Hosting

GitHub Pages (Settings → Pages → Source: GitHub Actions). The workflow passes
the Pages origin and base path to the build (`SITE_URL`, `BASE_PATH`), so it
works both at `https://<user>.github.io/<repo>/` and on a custom domain. For a
custom domain, set it in Settings → Pages and add `public/CNAME`.
