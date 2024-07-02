from abc import ABC


class MicrobialHealthIndexStrategy(ABC):
    def calculate(self, *kwargs) -> dict:
        raise NotImplementedError("Implement calculate method")
