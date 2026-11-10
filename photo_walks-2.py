# === Stage 2: Проверка полей ===
# Project: PhotoWalks
import re


def normalize_walk_name(raw):
    """Нормализует название прогулки: убирает лишние пробелы и приводит к Title Case."""
    cleaned = re.sub(r"\s+", " ", raw).strip()
    return cleaned.title() if cleaned else cleaned


def normalize_district(raw):
    """Нормализует район: убирает лишние пробелы и приводит к Title Case."""
    cleaned = re.sub(r"\s+", " ", raw).strip()
    return cleaned.title() if cleaned else cleaned


def normalize_time_of_day(raw):
    """Нормализует время суток к одному из допустимых значений."""
    mapping = {
        "утро": "утро",
        "день": "день",
        "вечер": "вечер",
        "ночь": "ночь",
    }
    cleaned = re.sub(r"\s+", " ", raw).strip().lower()
    if cleaned in mapping:
        return mapping[cleaned]
    return None


def normalize_duration(raw):
    """Нормализует длительность в минуты, принимает строки и числа."""
    if isinstance(raw, (int, float)):
        return int(raw)
    cleaned = re.sub(r"[^0-9]", "", str(raw).strip())
    if not cleaned:
        return None
    return int(cleaned)


def validate_walk(walk):
    """Проверяет поля сущности прогулки и возвращает список сообщений об ошибках.

    walk — словарь с полями name, district, time_of_day, duration.
    Возвращает список строк с ошибками (пустой список, если всё верно).
    """
    errors = []

    name = normalize_walk_name(walk.get("name", ""))
    if not name:
        errors.append("Название прогулки не может быть пустым.")
    else:
        walk["name"] = name

    district = normalize_district(walk.get("district", ""))
    if not district:
        errors.append("Район не может быть пустым.")
    else:
        walk["district"] = district

    time_of_day = normalize_time_of_day(walk.get("time_of_day", ""))
    if time_of_day is None:
        errors.append("Время суток должно быть одним из: утро, день, вечер, ночь.")
    else:
        walk["time_of_day"] = time_of_day

    duration = normalize_duration(walk.get("duration", ""))
    if duration is None:
        errors.append("Длительность должна быть числом минут.")
    elif duration <= 0:
        errors.append("Длительность должна быть положительным числом минут.")
    else:
        walk["duration"] = duration

    return errors
