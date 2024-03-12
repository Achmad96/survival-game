class Entity:
    def __init__(self, name, health, power):
        self.__name = name
        self.__health = health
        self.__power = power

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    @property
    def positionX(self):
        return self.__positionX

    @property
    def positionY(self):
        return self.__positionY

    def setPosition(self, x, y):
        self.__positionX = x
        self.__positionY = y