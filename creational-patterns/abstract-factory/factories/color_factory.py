from ..colors import Red, Green, Blue
from ..color import Color


class ColorFactory:
    def get_color(self, option: str) -> Color | None:
        color = None
        match option:
            case "red":
                color = self.get_red()
            case "green":
                color = self.get_green()
            case "blue":
                color = self.get_blue()
        return color

    @staticmethod
    def get_red() -> Color:
        return Red()

    @staticmethod
    def get_green() -> Color:
        return Green()

    @staticmethod
    def get_blue() -> Color:
        return Blue()
