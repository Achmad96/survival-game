import random

from pynput.keyboard import Key, Listener
from Entity import Entity
from Object import Place,HealPlace

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

        self.objects = []
        self.setObjectPosition(self.player.x, self.player.y, self.player)

        self.position_exemptions = [[self.player.x, self.player.y]]

        self.generateRandomObjects()
        self.printBoard()

    # the rendering function has been completed but may be too slow
    def render(self, vector):
        match vector:
            case "x":
                for i in range(len(self.board)):
                    self.board[i].extend(self.empty for _ in range(5))
                self.width += 5
            case "y":
                self.board.extend(list(list(self.empty for _ in range(self.width)) for _ in range(5)))
                self.height += 5
        self.generateRandomObjects()

    def generateRandomObjects(self):
        things = ["z","s","c", "h"]
        chance = [ 0.3, 0.3, 0.2, 0.2]
        results = random.choices(things, chance, k = 5)
        object: Entity | HealPlace = None

        for e in results:
            eY = random.choice(list(range(0, self.height - 1)))
            eX = random.choice(list(range(0, self.width - 1)))
            while ([eX, eY] in self.position_exemptions):
                eY = random.choice(list(range(0, self.height - 1)))
                eX = random.choice(list(range(0, self.width - 1)))
            match e:
                case "z": object = Entity("Z", 50, 10)
                case "s": object = Entity("S",60,20)
                case "c": object = Entity("C",70,30)
                case "h": object = HealPlace("H",70,30)
            object.setPosition(eX, eY)
            self.setObjectPosition(eX, eY, object)
            self.objects.append(object)
            self.position_exemptions.append([eX, eY])

    def validate(self):
        for e in list(self.objects):
            if self.player.x == e.x and self.player.y == e.y: 
                if type(e) == HealPlace:
                    e.heal(self.player)
                    self.objects.remove(e)
                elif type(e) == Entity:
                    self.player.health = self.player.health - e.power
                    self.objects.remove(e)


    def printBoard(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        enemiesCount = len(list(filter(lambda x: type(x) == Entity, self.objects)))
        print(f"""
--- YOU ---
health: {self.player.health}
power: {self.player.power}
-----------

Enemies: {enemiesCount}
""")
        
        for i in range(len(self.board)):
            print(f"{self.board[i]}", end="\n")
        print("\n\n")
        if self.player.health <= 0:
            print("[Log] You lose!")
            exit(0)
        elif enemiesCount == 0:
            print("[Log] You win!")
            exit(0)


    def movePlayer(self, x, y):
        if y < 0 or x < 0: return
        
        if x > self.width - 1: 
            self.render('x')

        if y > self.height - 1:
            self.render('y')
        # remove player from previous position
        self.setObjectPosition(x, y, self.empty)

        # add player to new position
        self.setObjectPosition(x, y, self.player)

        self.validate()
        self.printBoard()

    def handle_move(self, way):
        match way:
            case Key.up: self.movePlayer(self.player.x, self.player.y -  1)
            case Key.left: self.movePlayer(self.player.x - 1, self.player.y)
            case Key.down: self.movePlayer(self.player.x, self.player.y + 1)
            case Key.right: self.movePlayer(self.player.x + 1, self.player.y)

    def setObjectPosition(self, x, y, e: Entity | HealPlace | str):
        if type(e) == Entity or type(e) == HealPlace:
            self.board[e.y][e.x] = self.empty
            e.setPosition(x,y)
            self.board[y][x] = e.name
        else: self.board[y][x] = e

game = Game(5,7)
with Listener(on_press = game.handle_move) as listener:
    listener.join()