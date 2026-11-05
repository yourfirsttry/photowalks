# === Stage 1: Каркас модуля ===
# Project: PhotoWalks
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Walk:
    """Сущность «прогулка»: название, район, время суток и длительность."""

    name: str
    district: str
    time_of_day: str
    duration: str
    points: List["Point"] = field(default_factory=list)

    def add_point(self, point: "Point") -> None:
        self.points.append(point)

    def __len__(self) -> int:
        return len(self.points)


@dataclass
class Point:
    """Точка фотопрогулки: место и лучшее время для съёмки."""

    name: str
    best_light: str


def create_demo_walks() -> List[Walk]:
    """Создаёт демонстрационные записи прогулок с точками."""

    morning = Walk(
        name="Рассвет у реки",
        district="Центральный",
        time_of_day="утро",
        duration="120 минут",
    )
    morning.add_point(Point(name="Пирс у набережной", best_light="золотой час"))
    morning.add_point(Point(name="Мост через реку", best_light="рассвет"))
    morning.add_point(Point(name="Скамейка в парке", best_light="мягкий свет"))

    evening = Walk(
        name="Закат в историческом районе",
        district="Исторический",
        time_of_day="вечер",
        duration="90 минут",
    )
    evening.add_point(Point(name="Старая площадь", best_light="закат"))
    evening.add_point(Point(name="Часовня", best_light="золотой час"))

    return [morning, evening]


def main() -> None:
    """Краткий вывод каркаса модуля PhotoWalks."""

    walks = create_demo_walks()

    print("PhotoWalks — планировщик фотопрогулок")
    print("=" * 40)

    for walk in walks:
        print(f"Прогулка: {walk.name}")
        print(f"  Район: {walk.district}")
        print(f"  Время суток: {walk.time_of_day}")
        print(f"  Длительность: {walk.duration}")
        print(f"  Точек: {len(walk)}")
        for point in walk.points:
            print(f"    — {point.name} (лучше: {point.best_light})")
        print()


if __name__ == "__main__":
    main()
