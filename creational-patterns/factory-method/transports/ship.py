from ..transport import Transport


class Ship(Transport):
    def deliver(self, destination: str) -> str:
        return f"The product delivered to {destination} via Ship"
