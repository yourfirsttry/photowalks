# === Stage 3: Хранилище в памяти ===
# Project: PhotoWalks
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Walk:
    """Прогулка: название, район, время суток и длительность."""

    id: str
    name: str
    district: str
    time_of_day: str
    duration_minutes: int


class WalkStore:
    """Хранилище прогулок в памяти."""

    def __init__(self) -> None:
        self._walks: Dict[str, Walk] = {}
        self._counter = 0

    def add(self, name: str, district: str, time_of_day: str, duration_minutes: int) -> Walk:
        """Добавить прогулку и вернуть её с автоматически сгенерированным id."""

        self._counter += 1
        walk = Walk(
            id=f"W{self._counter:04d}",
            name=name,
            district=district,
            time_of_day=time_of_day,
            duration_minutes=duration_minutes,
        )
        self._walks[walk.id] = walk
        return walk

    def get(self, walk_id: str) -> Optional[Walk]:
        """Получить прогулку по id, если её нет — вернуть None."""

        return self._walks.get(walk_id)

    def list_walks(self) -> List[Walk]:
        """Вернуть все прогулки в порядке добавления."""

        return list(self._walks.values())


def demo() -> None:
    store = WalkStore()
    store.add("Рассвет на набережной", "Центральный", "утро", 45)
    found = store.get("W0001")
    print(f"Получено: {found.name} в районе {found.district}")
    for walk in store.list_walks():
        print(f"{walk.id} — {walk.name}, {walk.duration_minutes} мин")
