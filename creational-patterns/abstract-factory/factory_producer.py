from abstract_factory import AbstractFactory
from factories import ColorFactory, ShapeFactory


class FactoryProducer:
    @staticmethod
    def get_factory(option: str) -> AbstractFactory | None:
        factory = None
        match option:
            case "color":
                factory = ColorFactory()
            case "shape":
                factory = ShapeFactory()
        return factory
