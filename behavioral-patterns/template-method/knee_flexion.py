from exercise_template import ExerciseTemplate


class KneeFlexion(ExerciseTemplate):
    def is_valid_frame(self, frame: dict) -> bool:
        """
        :param frame: {
            "is_knee_visible": bool,
            "is_hip_visible": bool,
            "is_ankle_visible": bool
        }
        :return: bool
        """
        return all(frame.values())

    def calculate_rom_score(self, angle: float) -> int:
        """
        :param angle: angle between knee, hip and ankle
        :return: int
        """
        if 45 <= angle <= 90:
            return 100
        else:
            return 30
