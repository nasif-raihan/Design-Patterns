from ..shape import Shape
from ..shapes import Line, Rectangle, Triangle


class ShapeFactory:
    def get_shape(self, option: str) -> Shape:
        shape = None
        match option:
            case "line":
                shape = self.get_line()
            case "triangle":
                shape = self.get_triangle()
            case "rectangle":
                shape = self.get_rectangle()
        return shape

    @staticmethod
    def get_line() -> Shape:
        return Line()

    @staticmethod
    def get_triangle() -> Shape:
        return Triangle()

    @staticmethod
    def get_rectangle() -> Shape:
        return Rectangle()
