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

        zombie = Entity("Z", 50, 10)
        skeleton = Entity("S", 60, 13)
        creeper = Entity("C", 70, 20)
        self.__entities = [zombie, skeleton, creeper]

        # update board
        self.__player.positionX = 0
        self.__player.positionY = 0
        self.__board[self.__player.positionY][self.__player.positionX] = self.__player.name

        self.generate_random_entities()
        self.print_board()

    def render(self, vector):
        match vector:
            case "x":
                for i in range(len(self.__board)):
                    self.__board[i].extend(self.__empty for _ in range(3))
                self.__width += 3
            case "y":
                self.__board.extend([[self.__empty for _ in range(self.__width)] for _ in range(3)])
                self.__height += 3

    def generate_random_entities(self, rangeY = [1,4], rangeX = [0,4]):
        for e in self.__entities:
            eY = random.randint(*rangeY)
            eX = random.randint(*rangeX)

            e.positionX = eX
            e.positionY = eY
            self.__board[eY][eX] = e.name

    def validate(self):
        for e in self.__entities:
            if self.__player.positionX == e.positionX and self.__player.positionY == e.positionY:
                self.__player.health = self.__player.health - e.power
                e.power = e.health - self.__player.power
                self.__entities.remove(e)

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(len(self.__board)):
            print(f"{self.__board[i]}", end="\n")
        print("\n\n")
        if self.__player.health <= 0:
            print("[Log] You lose!")
            exit(0)
        elif len(self.__entities) == 0:
            print("[Log] You win!")
            exit(0)


    def __move_player(self, x, y):
        if y < 0 or x < 0: return

        if x > self.__width - 2: 
            self.render('x')

        if y > self.__height - 2:
            self.render('y')
        # remove player from previous position
        self.__board[self.__player.positionY][self.__player.positionX] = self.__empty

        # add player to new position
        self.__player.positionX = x
        self.__player.positionY = y
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