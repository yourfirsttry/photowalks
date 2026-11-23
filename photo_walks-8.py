# === Stage 8: Фильтрация записей ===
# Project: PhotoWalks
from datetime import datetime


def filter_walks_by_district(walks, district):
    return [walk for walk in walks if walk.get("district") == district]


def parse_date(value):
    return datetime.strptime(value, "%Y-%m-%d").date()


def filter_walks_by_date_range(walks, start_date, end_date):
    start = parse_date(start_date)
    end = parse_date(end_date)
    return [
        walk for walk in walks
        if start <= parse_date(walk["date"]) <= end
    ]


def filter_walks(walks, district=None, start_date=None, end_date=None):
    result = walks
    if district is not None:
        result = filter_walks_by_district(result, district)
    if start_date is not None:
        result = filter_walks_by_date_range(
            result, start_date, end_date
        )
    return result


if __name__ == "__main__":
    sample_walks = [
        {"name": "Парк у реки", "district": "Центральный", "date": "2024-05-10"},
        {"name": "Кольцо", "district": "Северный", "date": "2024-05-12"},
        {"name": "Тихий квартал", "district": "Центральный", "date": "2024-06-01"},
    ]

    print("Все прогулки:")
    for walk in sample_walks:
        print(walk)

    print("\nПрогулки в Центральном:")
    for walk in filter_walks(sample_walks, district="Центральный"):
        print(walk)

    print("\nПрогулки с 10.05 по 11.05:")
    for walk in filter_walks(sample_walks, start_date="2024-05-10", end_date="2024-05-11"):
        print(walk)
