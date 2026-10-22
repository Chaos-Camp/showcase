import kebabCase from 'lodash/kebabCase.js'

/** The longest slug the redirector will store. */
export const SLUG_MAX = 32

/** A slug is lowercase letters, digits and single dashes, and never starts or ends with a dash. */
export function isSlug(s: string): boolean {
  return /^[a-z0-9]+(-[a-z0-9]+)*$/.test(s)
}

/**
 * A slug for a page, from its title: lowercase words joined by dashes, cut at a word boundary to
 * fit `SLUG_MAX`. A title with no letters or digits has no slug.
 */
export function slugFor(title: string): string | null {
  const words = kebabCase(title.normalize('NFKD').replace(/[̀-ͯ]/g, '')).split('-').filter(Boolean)
  let slug = ''
  for (const word of words) {
    const next = slug ? `${slug}-${word}` : word
    if (next.length > SLUG_MAX) break
    slug = next
  }
  return slug || null
}
