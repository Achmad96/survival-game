import random

from pynput.keyboard import Key, Listener
from Entity import Entity

import os

class Game:
    def __init__(self, width, height):
        # create game board
        self.width = width
        self.height = height
    
        self.empty = " "
        self.board = [[self.empty for _ in range(width)] for _ in range(height)]

        # initialize entities
        self.player = Entity("P", 100, 100)
        self.player.setPosition(0, 0)

        self.entities = []
        self.setEntityPosition(self.player.x, self.player.y, self.player)

        self.position_exemptions = [[self.player.x, self.player.y]]

        self.generateRandomEntities()
        self.printBoard()

    # the rendering function has been completed but may be too slow
    def render(self, vector):
        match vector:
            case "x":
                for i in range(len(self.board)):
                    self.board[i].extend(self.empty for _ in range(2))
                self.width += 2
            case "y":
                self.board.extend([[self.empty for _ in range(self.width)] for _ in range(3)])
                self.height += 2
        self.generateRandomEntities()

    def generateRandomEntities(self):
        things = ["z","s","c"]
        chance = [ 50, 30, 20]
        results = random.choices(things, chance, k = 5)
        entity: Entity = None

        for e in results:
            eY = random.choice(list(range(0, self.height - 1)))
            eX = random.choice(list(range(0, self.width - 1)))
            while ([eX, eY] in self.position_exemptions):
                eY = random.choice(list(range(0, self.height - 1)))
                eX = random.choice(list(range(0, self.width - 1)))
            match e:
                case "z": entity = Entity("Z", 50, 10)
                case "s": entity = Entity("S",60,20)
                case "c": entity = Entity("C",70,30)
            entity.setPosition(eX, eY)
            self.setEntityPosition(eX, eY, entity)
            self.entities.append(entity)
            self.position_exemptions.append([eX, eY])

    def validate(self):
        for e in self.entities:
            if self.player.x == e.x and self.player.y == e.y:
                self.player.health = self.player.health - e.power
                self.entities.remove(e)


    def printBoard(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
--- YOU ---
health: {self.player.health}
power: {self.player.power}
-----------
""")
        for i in range(len(self.board)):
            print(f"{self.board[i]}", end="\n")
        print("\n\n")
        if self.player.health <= 0:
            print("[Log] You lose!")
            exit(0)
        if len(self.entities) == 0:
            print("[Log] You win!")
            exit(0)


    def movePlayer(self, x, y):
        if y < 0 or x < 0: return
        
        if x > self.width - 1: 
            self.render('x')

        if y > self.height - 1:
            self.render('y')
        # remove player from previous position
        self.setEntityPosition(x, y, self.empty)

        # add player to new position
        self.setEntityPosition(x, y, self.player)

        self.validate()
        self.printBoard()

    def handle_move(self, way):
        match way:
            case Key.up: self.movePlayer(self.player.x, self.player.y -  1)
            case Key.left: self.movePlayer(self.player.x - 1, self.player.y)
            case Key.down: self.movePlayer(self.player.x, self.player.y + 1)
            case Key.right: self.movePlayer(self.player.x + 1, self.player.y)

    def setEntityPosition(self, x, y, e: Entity | str):
        if type(e) == Entity:
            self.board[e.y][e.x] = self.empty
            e.setPosition(x,y)
            self.board[y][x] = e.name
        else: self.board[y][x] = e

game = Game(5,7)
with Listener(on_press = game.handle_move) as listener:
    listener.join()