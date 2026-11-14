# === Stage 4: Редактирование записей ===
# Project: PhotoWalks
from typing import Any, Dict, List, Optional

WALK_FIELDS: Dict[str, Any] = {
    "title": str,
    "district": str,
    "time_of_day": str,
    "duration": int,
}

ALLOWED_TIME_OF_DAY: List[str] = [
    "dawn",
    "morning",
    "noon",
    "afternoon",
    "evening",
    "night",
]

DEFAULT_DURATIONS: List[int] = [15, 20, 30, 45, 60, 90]


def is_valid_time_of_day(value: Any) -> bool:
    return value in ALLOWED_TIME_OF_DAY


def is_valid_duration(value: Any) -> bool:
    return isinstance(value, int) and value > 0 and value in DEFAULT_DURATIONS


def is_valid_title(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def is_valid_district(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def validate_walk_fields(changes: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    if not isinstance(changes, dict):
        return ["changes must be a dictionary"]
    for field, value in changes.items():
        if field not in WALK_FIELDS:
            errors.append(f"unknown field: {field}")
            continue
        validator = WALK_FIELDS[field]
        if validator is str:
            if not is_valid_title(value):
                errors.append(f"invalid title: {value!r}")
        elif field == "district":
            if not is_valid_district(value):
                errors.append(f"invalid district: {value!r}")
        elif field == "time_of_day":
            if not is_valid_time_of_day(value):
                errors.append(f"invalid time_of_day: {value!r}")
        elif field == "duration":
            if not is_valid_duration(value):
                errors.append(f"invalid duration: {value!r}")
    return errors


def apply_walk_changes(walk: Dict[str, Any], changes: Dict[str, Any]) -> bool:
    errors = validate_walk_fields(changes)
    if errors:
        return False
    for field, value in changes.items():
        if field in WALK_FIELDS:
            walk[field] = value
    return True
