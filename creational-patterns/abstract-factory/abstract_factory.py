from abc import ABC, abstractmethod

from color import Color
from shape import Shape


class AbstractFactory(ABC):
    @abstractmethod
    def get_color(self, option: str) -> Color:
        raise NotImplementedError("Implement get_color method")

    @abstractmethod
    def get_shape(self, option: str) -> Shape:
        raise NotImplementedError("Implement get_shape method")
