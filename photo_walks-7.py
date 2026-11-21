# === Stage 7: Генерация идентификаторов ===
# Project: PhotoWalks
PROJECT_ID_PREFIX = "pw"


def generate_unique_id(prefix, existing_ids):
    base = f"{prefix}-{len(existing_ids) + 1}"
    candidate = base
    counter = 1
    while candidate in existing_ids:
        candidate = f"{prefix}-{len(existing_ids) + 1}-{counter}"
        counter += 1
    existing_ids.add(candidate)
    return candidate


def make_id(prefix, existing_ids):
    return generate_unique_id(prefix, set(existing_ids))
