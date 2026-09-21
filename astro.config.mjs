// @ts-check
import { defineConfig } from "astro/config";

// GitHub Pages: the deploy workflow sets SITE_URL and BASE_PATH (e.g. "/qbasisdotone_hp").
// Locally both are unset and the site serves from "/".
export default defineConfig({
  site: process.env.SITE_URL,
  base: process.env.BASE_PATH || "/",
  trailingSlash: "ignore",
});
