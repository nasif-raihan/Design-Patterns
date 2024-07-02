from exercise_template import ExerciseTemplate


class ShoulderExtension(ExerciseTemplate):
    def is_valid_frame(self, frame: dict) -> bool:
        """
        :param frame: {
            "is_shoulder_visible": bool,
            "is_elbow_visible": bool,
            "is_wrist_visible": bool
        }
        :return: bool
        """
        return all(frame.values())

    def calculate_rom_score(self, angle: float) -> int:
        """
        :param angle: angle between shoulder, elbow and wrist
        :return: int
        """
        if 165 <= angle <= 180:
            return 100
        else:
            return 30
