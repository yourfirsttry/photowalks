# === Stage 5: Удаление и восстановление ===
# Project: PhotoWalks
import uuid


class Walk:
    """Прогулка с поддержкой мягкого удаления и восстановлением."""

    def __init__(self, title, district, time_of_day, duration, walk_id=None):
        self.id = walk_id or uuid.uuid4().hex
        self.title = title
        self.district = district
        self.time_of_day = time_of_day
        self.duration = duration
        self.deleted = False

    def hard_delete(self):
        """Полное удаление сущности — сущность исчезает из системы."""
        raise ValueError(
            f"Прогулка '{self.title}' удалена навсегда и не может быть восстановлена"
        )

    def soft_delete(self):
        """Мягкое удаление: сущность остаётся в хранилище, но становится неактивной."""
        self.deleted = True

    @property
    def is_active(self):
        return not self.deleted

    def restore(self):
        """Восстановить ранее мягко удалённую прогулку."""
        self.deleted = False

    def __repr__(self):
        status = "удалена" if self.deleted else "активна"
        return f"<Walk {self.id!r} '{self.title}' [{status}]>"
