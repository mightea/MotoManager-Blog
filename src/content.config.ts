import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// One Markdown file per monthly release post: src/content/posts/release-YYYYMM.md
// Patch releases are appended to the month's post as new "### version – date" sections.
const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    // Newest version of each component covered by the post.
    versions: z.object({
      web: z.string().optional(),
      ios: z.string().optional(),
    }),
    draft: z.boolean().default(false),
  }),
});

export const collections = { posts };
