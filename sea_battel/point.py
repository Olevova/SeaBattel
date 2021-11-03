#создаем простейший кдасс игры. Точка
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):# метод сравнения точки
       return (self.x,self.y) == other

    def __repr__(self): #метод печати точки
        return f"{self.x}, {self.y}"





