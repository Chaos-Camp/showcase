"""The weekly clicks report: the busiest links and how many clicks each had."""

from collections import Counter

from jinja2 import Environment

TOP = 5
# As long as the longest slug (SLUG_MAX in ts/src/slug.ts), so the counts line up.
SLUG_WIDTH = 40

TEMPLATE = Environment(autoescape=False, trim_blocks=True, lstrip_blocks=True).from_string(
    """\
clicks, week of {{ week }}: {{ total }}
{% for slug, n in top %}
  {{ "%-*s"|format(width, slug) }} {{ "%5d"|format(n) }}{% if titles.get(slug) %}  {{ titles[slug] }}{% endif %}
{% else %}
  no clicks this week
{% endfor %}
"""
)


def busiest(events, top=TOP):
    """The `top` slugs with the most clicks, most first, ties by slug."""
    counts = Counter(e["slug"] for e in events if e.get("kind") == "click")
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:top]


def weekly(events, week, titles=None):
    """The report for one week of redirector events; `titles` maps a slug to its page's title."""
    clicks = [e for e in events if e.get("kind") == "click"]
    return TEMPLATE.render(week=week, total=len(clicks), top=busiest(clicks), width=SLUG_WIDTH, titles=titles or {})
