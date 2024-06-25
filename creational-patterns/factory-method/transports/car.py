from ..transport import Transport


class Car(Transport):
    def deliver(self, destination: str) -> str:
        return f"The product delivered to {destination} via Car"
