import { getCollection, type CollectionEntry } from "astro:content";

export type Post = CollectionEntry<"posts">;

export async function getPosts(): Promise<Post[]> {
  const posts = await getCollection("posts", ({ data }) => !data.draft);
  return posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}

/** URL path relative to the site base, e.g. "2026/11/release-202611/". */
export function postPath(post: Post): string {
  const d = post.data.date;
  const yyyy = d.getUTCFullYear();
  const mm = String(d.getUTCMonth() + 1).padStart(2, "0");
  return `${yyyy}/${mm}/${post.id}/`;
}

/** Prefix a site-relative path with the configured base. */
export function withBase(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, "");
  return `${base}/${path.replace(/^\//, "")}`;
}

export function formatDate(d: Date): string {
  return d.toLocaleDateString("en-GB", {
    day: "numeric",
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  });
}
