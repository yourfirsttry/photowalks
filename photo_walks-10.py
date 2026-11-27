# === Stage 10: Текстовый поиск ===
# Project: PhotoWalks
import re


def highlight_text(text, highlight):
    if not text or not highlight:
        return text

    escaped_highlight = re.escape(str(highlight))
    pattern = re.compile(escaped_highlight, re.IGNORECASE)

    def _replace(match):
        return ' ' + match.group(0) + ' '

    highlighted = pattern.sub(_replace, str(text))
    return highlighted


def find_walk_by_text(walks, field, term):
    results = []
    for walk in walks:
        value = getattr(walk, field, None)
        if value and str(term).lower() in str(value).lower():
            results.append(walk)
    return results


def find_walk_by_title(walks, term):
    return find_walk_by_text(walks, 'name', term)
