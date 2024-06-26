from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        raise NotImplementedError("Implement draw method")
