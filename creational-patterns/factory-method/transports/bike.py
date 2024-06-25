from ..transport import Transport


class Bike(Transport):
    def deliver(self, destination: str) -> str:
        return f"The product delivered to {destination} via Bike"
