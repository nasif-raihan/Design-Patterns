from abc import ABC, abstractmethod


class ExerciseTemplate(ABC):
    def classify_health(self, frame: dict, angle: float) -> str:
        if not self.is_valid_frame(frame):
            return "Invalid frame"

        range_of_motion_score = self.calculate_rom_score(angle)
        if range_of_motion_score < 40:
            return "Unhealthy"
        else:
            return "Healthy"

    @abstractmethod
    def is_valid_frame(self, frame: dict) -> bool:
        raise NotImplementedError("Implement is_valid_frame method")

    @abstractmethod
    def calculate_rom_score(self, angle: float) -> int:
        raise NotImplementedError("Implement calculate_rom_score method")
