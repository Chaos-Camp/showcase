import assert from 'node:assert/strict'
import { test } from 'node:test'
import { SLUG_MAX, isSlug, slugFor } from '../src/slug.ts'

test('a slug is lowercase words joined by single dashes', () => {
  assert.ok(isSlug('hello-world'))
  assert.ok(!isSlug('Hello'))
  assert.ok(!isSlug('-edge'))
  assert.ok(!isSlug('two--dashes'))
})

test('a title becomes a slug', () => {
  assert.equal(slugFor('Hello, World!'), 'hello-world')
  assert.equal(slugFor('Café au lait'), 'cafe-au-lait')
  assert.equal(slugFor('!!!'), null)
})

test('a long title is cut at a word, within the limit', () => {
  const slug = slugFor('The quick brown fox jumps over the lazy dog again and again')!
  assert.ok(slug.length <= SLUG_MAX)
  assert.ok(isSlug(slug))
  assert.equal(slug, 'the-quick-brown-fox-jumps-over-the-lazy')
})
