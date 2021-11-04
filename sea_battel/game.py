#импортирем классы для создания класса самой игры
import random
import time
from ship import Ship
from player import *
from sea_battel import Board


class Game():#класс самой игры, то место где все склеиваем в кучу
    def __init__(self):
        R = "make your board random push yes,for no push any buttom. better push no "
        print(R.upper().center(150))#прикручиваем возможность играку ставить корабли самому. Есть нюансы
        ans = input().upper()
        if ans.isalpha() and ans == "YES":
            c = self.choise_place()
        else:
            c = self.random_board()
        c2 = self.random_board()
        self.play = Comp(c, c2)
        self.play2 = You(c2, c)
        c2.hidden = True

    def random_board(self): #метод генерирования доски с кораблями на основе метода random_place()
        board = None
        while board is None:
            board = self.random_place()
        return board

    def choise_place(self):#метод установки кораблей на свой вкус.не доработан
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        print("Please add ship ")
        for l in lens:
            print(l)
            a = input("input Point of the ship nose :").split()
            b = input("ship position 0 -vertical, 1 Horizont :")
            ship = Ship(l, Point(int(a[0])-1, int(a[1])-1), int(b))
            try:
                board.ship_plus(ship)
                print(board.field)
            except BoardBusyException as e:
                print (e)
            print(board)
        board.begin()
        return board

    def random_place(self):#метод рандомного становления кораблей
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(l, Point(randint(0, 6), randint(0, 6)), randint(0, 1))
                try:
                    board.ship_plus(ship)
                    break
                except BoardBusyException:
                    pass
        board.begin()
        return board

    def loop(self):#метод запуска игры
        l = 2
        while True:
            fras = ["Its your chance", "Go - Go", "Do it", "You are weak"]#словарь с рандомными фразами далие по игре
            print(10*" "+'Computer Board')
            print(self.play2.board)
            print("🛥"*22)
            print(10*" "+'Your board')
            print(self.play.board)
            print("🛥" * 22)
            if l%2 == 0:
                print(f"{fras[random.randint(0,3)]}")
                repeat = self.play2.move()
                time.sleep(1)
            elif l%2 == 1:
                repeat = self.play.move()
                time.sleep(2)
            if repeat:
                l -= 1
            if self.play2.board.count == 7:
                print("You win, congratulation!!!")
                break
            if self.play.board.count == 7:
                print("You win, congratulation!!!")
                break
            l += 1

    def meet(self):#метод приветствия игрока, плюс короткая справка по игре
        y = Board()
        text = """The game is played on two grids, one for each player. 
        The grids are typically square – usually 6×6 – and the individual squares in the grid are identified by number.
        On one grid the player arranges ships. Every player must arranges 7 ships(programme make it automatic). 
        Every player make move. He print coordinates in accordance with his move. If move in goal, he make next move again.
        If not, it makes next player. Win who first defeated all ships """
        print("\t""         Informations about game")
        print("\t", "                RuleS",
              "\n""______________________________________________________________________________")
        print(f"{text}")
        print("■■■ - 1 ship")
        print("♠♠ - 2 ships")
        print("● - 4 ships")
        print()
        print("""You see grid, there are - space for marks""")
        print(y)
        print()

    def the_end(self):#конец игры.Есть возможность сыграть сново
        print("If you want to play again, print Yes, if not No")
        t = input().upper()
        if t.isalpha() and t == 'YES':
            return self.start_game()
        else:
            return "THE END"

    def start_game(self): #метод запуска. поехали играть
        self.meet()
        self.loop()
        self.the_end()

#g = Game()
#print(g.play.move())
#print(g.play.board)
#print(g.play2.move())
#print(g.play2.board)
#print(g.play.move())
#print(g.play.board)
#print(g.play2.move())
#print(g.play2.board)
g = Game()
g.start_game()
