import assert from 'node:assert/strict'
import { test } from 'node:test'
import { isSlug } from '../src/slug.ts'

test('a slug is lowercase words joined by single dashes', () => {
  assert.ok(isSlug('hello-world'))
  assert.ok(!isSlug('Hello'))
  assert.ok(!isSlug('-edge'))
  assert.ok(!isSlug('two--dashes'))
})
