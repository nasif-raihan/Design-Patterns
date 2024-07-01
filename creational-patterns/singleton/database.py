from typing import Self


class Database:
    __instance = None

    def __init__(self):
        if self.__instance:
            raise RuntimeError("An instance of Database is already running.")

    @classmethod
    def get_instance(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = Database()
            print("Creating a Database instance.")
        print(f"{id(cls.__instance)=}\n")
        return cls.__instance


if __name__ == "__main__":
    # Reference ID of both the connection should be the same.
    print("Connection 1")
    connection_1 = Database.get_instance()
    print("Connection 2")
    connection_2 = Database.get_instance()

    # This will raise a runtime error!
    print("Connection 3")
    connection_3 = Database()
