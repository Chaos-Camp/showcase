"""The weekly clicks report: the busiest links and how many clicks each had."""

from collections import Counter

from jinja2 import Environment

TOP = 5

TEMPLATE = Environment(autoescape=False, trim_blocks=True, lstrip_blocks=True).from_string(
    """\
clicks, week of {{ week }}: {{ total }}
{% for slug, n in top %}
  {{ "%-32s"|format(slug) }} {{ "%5d"|format(n) }}
{% else %}
  no clicks this week
{% endfor %}
"""
)


def busiest(events, top=TOP):
    """The `top` slugs with the most clicks, most first, ties by slug."""
    counts = Counter(e["slug"] for e in events if e.get("kind") == "click")
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:top]


def weekly(events, week):
    """The report for one week of redirector events."""
    clicks = [e for e in events if e.get("kind") == "click"]
    return TEMPLATE.render(week=week, total=len(clicks), top=busiest(clicks))
