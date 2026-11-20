import rss from "@astrojs/rss";
import type { APIContext } from "astro";
import { getPosts, postPath, withBase } from "../lib/posts";

export async function GET(context: APIContext) {
  const posts = await getPosts();
  return rss({
    title: "MotoManager Releases",
    description: "Release notes for the MotoManager web app and iOS app.",
    site: new URL(import.meta.env.BASE_URL, context.site!).href,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.updated ?? post.data.date,
      link: withBase(postPath(post)),
    })),
  });
}
