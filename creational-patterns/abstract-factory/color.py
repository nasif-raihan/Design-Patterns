from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def fill(self) -> str:
        raise NotImplementedError("Implement fill method")
