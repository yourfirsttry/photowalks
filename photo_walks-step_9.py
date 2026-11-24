# === Stage 9: Сортировка записей ===
# Project: PhotoWalks
from datetime import datetime


def parse_date(value):
    if value is None:
        return datetime.min
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d.%m.%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    return datetime.min


def sort_walks(walks, key="name", ascending=True):
    if key == "name":
        return sorted(
            walks,
            key=lambda walk: (walk.get("created_at") is None, walk.get("name", "")),
            reverse=not ascending,
        )
    if key == "created_at":
        return sorted(
            walks,
            key=lambda walk: parse_date(walk.get("created_at")),
            reverse=not ascending,
        )
    return sorted(walks, reverse=not ascending)


def walk_by_name(walks, name):
    for walk in walks:
        if str(walk.get("name", "")).lower() == str(name).lower():
            return walk
    return None


def walk_by_id(walks, walk_id):
    for walk in walks:
        if walk.get("id") == walk_id:
            return walk
    return None


def add_walk(walks, walk):
    walk["id"] = walk.get("id")
    if "created_at" not in walk:
        walk["created_at"] = datetime.now().isoformat()
    walks.append(walk)
    return walk


def remove_walk(walks, walk_id):
    for index, walk in enumerate(walks):
        if walk.get("id") == walk_id:
            return walks.pop(index)
    return None


def get_walks(walks, key="name", ascending=True):
    return sort_walks(walks, key=key, ascending=ascending)
