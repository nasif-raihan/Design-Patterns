from transport import Transport


from transports import Bike, Car, Ship


class TransportFactory:
    def get_transport(self, option: str) -> Transport | None:
        transport = None
        match option:
            case "land":
                transport = self.get_car()
            case "water":
                transport = self.get_ship()
            case "popular":
                transport = self.get_bike()
        return transport

    @staticmethod
    def get_bike() -> Transport:
        return Bike()

    @staticmethod
    def get_car() -> Transport:
        return Car()

    @staticmethod
    def get_ship() -> Transport:
        return Ship()
