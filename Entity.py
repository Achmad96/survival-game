class Entity:
    def __init__(self, name: str, health: int, power: int):
        self.__name = name
        self.__health = health
        self.__power = power

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int):
        self.__health = health

    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, power: int):
        self.__power = power

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def setPosition(self, x: int, y: int):
        self.__x = x
        self.__y = y