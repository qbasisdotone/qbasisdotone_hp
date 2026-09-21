import ko from "../content/ko.json";
import en from "../content/en.json";
import site from "../content/site.json";

import koHero from "../content/snippets/ko/hero.py?raw";
import enHero from "../content/snippets/en/hero.py?raw";
import koVqe from "../content/snippets/ko/vqe.py?raw";
import enVqe from "../content/snippets/en/vqe.py?raw";
import koCompare from "../content/snippets/ko/compare.py?raw";
import enCompare from "../content/snippets/en/compare.py?raw";

export const locales = ["ko", "en"] as const;
export type Locale = (typeof locales)[number];
export type Copy = typeof ko;

// en.json must have exactly the same shape as ko.json; this line fails the type check otherwise.
const copies: Record<Locale, Copy> = { ko, en };
const snippets = {
  ko: { hero: koHero, vqe: koVqe, compare: koCompare },
  en: { hero: enHero, vqe: enVqe, compare: enCompare },
};

export const t = (locale: Locale) => copies[locale];
export const code = (locale: Locale) => snippets[locale];
export { site };

/** Prefix a path under public/ (or a page path) with the deploy base, e.g. "/qbasisdotone_hp/". */
export function asset(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/?$/, "/");
  return base + path.replace(/^\//, "");
}

export const homeOf = (locale: Locale) => asset(locale === "ko" ? "" : "en/");
