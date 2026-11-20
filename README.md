# MotoManager Releases

Release notes blog for the MotoManager web app (`MotoManager`), API
(`MotoManagerApi`) and iOS app (`MotoManagerApp`). Static Astro site, deployed
to GitHub Pages by `.github/workflows/deploy.yml` on every push to `main`.

## Writing

- **One post per month**: `src/content/posts/release-YYYYMM.md`, published at
  `/YYYY/MM/release-YYYYMM/`. Frontmatter: `title`, `description`, `date`,
  optional `updated`, `versions: { web, api, ios }` (newest version covered),
  optional `draft: true`.
- Structure: Upgrade notes → Highlights (hand-written) → Security → one `##`
  section per component with a `### <version> – <Month day>` section per release.
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

## Hosting

GitHub Pages (Settings → Pages → Source: GitHub Actions). The workflow passes
the Pages origin and base path to the build (`SITE_URL`, `BASE_PATH`), so it
works both at `https://<user>.github.io/<repo>/` and on a custom domain. For a
custom domain, set it in Settings → Pages and add `public/CNAME`.
