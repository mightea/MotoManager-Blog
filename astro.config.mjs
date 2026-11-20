// @ts-check
import { defineConfig } from "astro/config";

// SITE_URL / BASE_PATH are set by the GitHub Pages workflow (from
// actions/configure-pages), so the same config works for
// https://<user>.github.io/<repo>/ and for a custom domain.
export default defineConfig({
  site: process.env.SITE_URL ?? "http://localhost:4321",
  base: process.env.BASE_PATH ?? "/",
  trailingSlash: "always",
  markdown: {
    shikiConfig: { theme: "github-dark" },
  },
});
