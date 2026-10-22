"""Click counts, from the events the redirector writes."""


def total_clicks(events):
    """How many clicks the events record."""
    return sum(1 for e in events if e.get("kind") == "click")
