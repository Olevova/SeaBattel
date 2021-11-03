#импорт нужных классов для дальнейше работы по созданию поля доски
from point import Point
from ship import Ship
from exseption import *
from random import randint

class Board(): #создаем класс доски
    def __init__(self, hidden=False):
        self.hidden = hidden
        self.count = 0
        self.field = [["0" for _ in range(6)] for _ in range(6)]
        self.ships_on = []
        self.occupied = []
        self.shooting = []
    def cort_out(self, poi): # проверка точки на попадание в поле
        return not ((0 <= poi.x < 6) and (0 <= poi.y < 6))

    def ship_plus(self, ship):# метод заноса кораблей на поле
        for poi in ship.make_ship:
            if self.cort_out(poi) or poi in self.occupied:
                raise BoardBusyException()
        for poi in ship.make_ship:
            if ship.lenght == 3: # создаем трехпалубный корабль
                self.field[poi.x][poi.y] = "■"
                self.occupied.append(poi)
            if ship.lenght == 2: # создаем двухпалубный корабль
                self.field[poi.x][poi.y] = "♠"
                self.occupied.append(poi)
            else:
                self.field[poi.x][poi.y] = "●" # одна палуба
                self.occupied.append(poi)
        self.ships_on.append(ship)
        self.near_ocupied(ship)

    def near_ocupied (self, ship, cell=False):# метод проверки точек рядом с корабльом(те которые занимать по правилам игры нельзя)
        buffer_point = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0 , 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for poi in ship.make_ship:
            for poix, poiy in buffer_point:
                con = Point(poi.x + poix, poi.y + poiy)
                if not (self.cort_out(con)) and con not in self.occupied:
                    if cell:
                        self.field[con.x][con.y] = "."
                    self.occupied.append(con)


    def shoot(self, sp): # делаем метод хода - выстрела по полю
        if self.cort_out(sp):
            raise BoardOutException
        if sp in self.occupied:
            raise BoardBusyException

        self.occupied.append(sp)
        for ship in self.ships_on:
            if sp in ship.make_ship:
                ship.life -= 1
                self.field[sp.x][sp.y] = "X"
                if ship.life == 0:
                    self.count += 1
                    self.near_ocupied(ship, cell=True)
                    print("ship defeated")
                    return True
                else:
                    print("ship is injure")
                    return True
        print("miss")
        self.field[sp.x][sp.y] = "*"
        return False

    def __str__(self): # отображение поля игры
        cort = ""
        cort += "        1 |  2 |  3 |  4 |  5 |  6 |"
        for i,b in zip(self.field, range(1,7)):
            cort += f"\n{b}"+"-----| " + ' |  '.join(i) + " | "
        if self.hidden:
            l = ["0","■","♠","●"]
            for i in l:
                if i in cort:
                    cort = cort.replace( i, "?")
        return cort

    def begin(self): # обнуляем список точек
        self.occupied = []


