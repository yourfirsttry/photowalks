# === Stage 6: Связанная сущность ===
# Project: PhotoWalks
"""Модуль PhotoWalks. Этап 6: сущность 'точка' и функции её добавления.

Точка связана с прогулкой по идентификатору прогулки. Модуль самостоятелен
и использует только стандартную библиотеку.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import time
from typing import Dict, List, Optional, Tuple


@dataclass
class Walk:
    """Прогулка: название, район, время суток, длительность."""

    name: str
    district: str
    time_of_day: time
    duration_minutes: int

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Название прогулки не может быть пустым")
        if self.duration_minutes <= 0:
            raise ValueError("Длительность прогулки должна быть положительной")


@dataclass
class Point:
    """Точка фотопрогулки.

    Связана с прогулкой через идентификатор прогулки.
    """

    walk_id: str
    name: str
    latitude: float
    longitude: float
    best_light: str = "золотой час"
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.walk_id:
            raise ValueError("Идентификатор прогулки не может быть пустым")
        if not self.name:
            raise ValueError("Название точки не может быть пустым")
        if not (-90.0 <= self.latitude <= 90.0):
            raise ValueError("Широта должна находиться в диапазоне [-90, 90]")
        if not (-180.0 <= self.longitude <= 180.0):
            raise ValueError("Долгота должна находиться в диапазоне [-180, 180]")


class PhotoWalks:
    """Контейнер прогулок и точек с функциями добавления."""

    def __init__(self) -> None:
        self._walks: Dict[str, Walk] = {}
        self._points: Dict[str, Point] = {}

    def add_walk(self, walk: Walk) -> str:
        """Добавить прогулку и вернуть её идентификатор."""
        if walk.walk_id in self._walks:
            raise ValueError(f"Прогулка с id '{walk.walk_id}' уже существует")
        self._walks[walk.walk_id] = walk
        return walk.walk_id

    def add_point(self, point: Point) -> str:
        """Добавить точку и вернуть её идентификатор."""
        if point.walk_id not in self._walks:
            raise ValueError(
                f"Прогулка с id '{point.walk_id}' не найдена. "
                f"Доступные id: {', '.join(sorted(self._walks)) or '(нет)'}"
            )
        if point.id in self._points:
            raise ValueError(f"Точка с id '{point.id}' уже существует")
        self._points[point.id] = point
        return point.id

    def get_point(self, point_id: str) -> Optional[Point]:
        """Вернуть точку по её идентификатору или None."""
        return self._points.get(point_id)

    def get_points_for_walk(self, walk_id: str) -> List[Point]:
        """Вернуть список точек для указанной прогулки."""
        return [
            point for point in self._points.values() if point.walk_id == walk_id
        ]

    def list_walks(self) -> List[Walk]:
        """Вернуть список всех прогулок."""
        return list(self._walks.values())

    def list_points(self) -> List[Point]:
        """Вернуть список всех точек."""
        return list(self._points.values())


if __name__ == "__main__":
    demo = PhotoWalks()
    demo.add_walk(Walk("Парк", "Центральный район", time(17, 30), 60))
    demo.add_point(Point("1", "Фонтан", 55.75, 37.61))
    demo.add_point(Point("2", "Скамейка", 55.76, 37.62, best_light="рассвет"))
    for point in demo.get_points_for_walk("1"):
        print(point.name, point.latitude, point.longitude, point.best_light)
