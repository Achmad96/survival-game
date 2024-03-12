import random

from pynput.keyboard import Key, Listener
from Entity import Entity

import os

class Game:
    def __init__(self, width, height):
        # create game board
        self.__width = width
        self.__height = height
    
        self.__empty = " "
        self.__board = [[self.__empty for _ in range(width)] for _ in range(height)]

        # initialize entities
        self.__player = Entity("P", 100, 100)
        self.__entities = []

        # update board
        self.__player.setPosition(0, 0)
        self.__board[self.__player.positionY][self.__player.positionX] = self.__player.name

        self.generate_random_entities()
        self.print_board()

    # the rendering function has been completed but may be too slow
    def render(self, vector):
        match vector:
            case "x":
                for i in range(len(self.__board)):
                    self.__board[i].extend(self.__empty for _ in range(2))
                self.__width += 2
            case "y":
                self.__board.extend([[self.__empty for _ in range(self.__width)] for _ in range(3)])
                self.__height += 2
        self.generate_random_entities()

    def generate_random_entities(self):
        things = ["z","s","c"]
        chance = [ 50, 30, 20]
        results = random.choices(things, chance, k = 5)
        for e in results:
            eY = random.randint(self.__height - 3, self.__height - 1)
            eX = random.randint(self.__width - 3, self.__width - 1)
            match e:
                case "z": 
                    zombie = Entity("Z", 50, 10)
                    zombie.setPosition(eX, eY)
                    self.__board[eY][eX] = zombie.name
                    self.__entities.append(zombie)
                case "s": 
                    skeleton = Entity("S",60,20)
                    skeleton.setPosition(eX, eY)
                    self.__board[eY][eX] = skeleton.name
                    self.__entities.append(skeleton)
                case "c": 
                    creeper = Entity("C",70,30)
                    creeper.setPosition(eX, eY)
                    self.__board[eY][eX] = creeper.name
                    self.__entities.append(creeper)

    def validate(self):
        for e in self.__entities:
            if self.__player.positionX == e.positionX and self.__player.positionY == e.positionY:
                self.__player.health = self.__player.health - e.power
                self.__entities.remove(e)

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
--- YOU ---
health: {self.__player.health}
power: {self.__player.power}
-----------
""")
        for i in range(len(self.__board)):
            print(f"{self.__board[i]}", end="\n")
        print("\n\n")
        if self.__player.health <= 0:
            print("[Log] You lose!")
            exit(0)
        if len(self.__entities) == 0:
            print("[Log] You win!")
            exit(0)


    def __move_player(self, x, y):
        if y < 0 or x < 0: return
        
        if x > self.__width - 1: 
            self.render('x')

        if y > self.__height - 1:
            self.render('y')
        # remove player from previous position
        self.__board[self.__player.positionY][self.__player.positionX] = self.__empty

        # add player to new position
        self.__player.setPosition(x,y)
        self.__board[y][x] = self.__player.name

        self.update_board()

    def handle_move(self, way):
        match way:
            case Key.up: self.__move_player(self.__player.positionX, self.__player.positionY -  1)
            case Key.left: self.__move_player(self.__player.positionX - 1, self.__player.positionY)
            case Key.down: self.__move_player(self.__player.positionX, self.__player.positionY + 1)
            case Key.right: self.__move_player(self.__player.positionX + 1, self.__player.positionY)

    def update_board(self):
        self.validate()
        self.print_board()

game = Game(5,7)

with Listener(on_press = game.handle_move) as listener:
    listener.join()