#создаем клас игрокаи дочернии от него классы игрок компютер и игрок Вы

from random import randint

from exseption import *
from point import Point


class Player():
    def __init__(self, myboard, board):
        self.board = myboard
        self.other = board

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.board.shoot(target)
                return repeat
            except BoardException as e:
                print(e)

class Comp(Player): #класс игрок компютер
    def __init__(self, myboard, board):
        Player.__init__(self, myboard, board)
        print("Hi, I am your computer, and I want play with you")

    def ask(self): #запрос хода компютера, ход вводится рандомно
        t = Point(randint(0, 5), randint(0, 5))
        print(f"PC move {t.x+1,t.y+1}")
        return t

class You(Player): #класс Вы игрок
    def ask(self): #запрос хода с проверками на 2 координаты, или являеться ввод цифрой, а также или попадают координаты в поле
        while True:
            cords = input(" Your move: ").split()
            if len(cords) != 2:
                print(" Type two cords! ")
                continue
            x, y = cords
            if not (x.isdigit()) or not (y.isdigit()):
                print(" It must be only number ")
                continue
            if not (1 <= int(x) <= 6) or not (1 <= int(y) <= 6):
                print(" numbers must be in a range 1-6 ")
                continue

            x, y = int(x), int(y)

            return Point(x - 1, y - 1)
