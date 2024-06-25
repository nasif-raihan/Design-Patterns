from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self, destination: str) -> str:
        raise NotImplementedError("Implement deliver method")
