/** A slug is lowercase letters, digits and single dashes, and never starts or ends with a dash. */
export function isSlug(s: string): boolean {
  return /^[a-z0-9]+(-[a-z0-9]+)*$/.test(s)
}
