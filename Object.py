from Entity import Entity
import random
class Place:
    def __init__(self, name, x, y):
        self.__name = name
        self.__x = x
        self.__y = y

    @property
    def name(self):
        return self.__name
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

class HealPlace(Place):
    def heal(self, player: Entity):
        health_number = random.choices([10, 20, 30],[0.7, 0.2, 0.1])
        player.health += health_number