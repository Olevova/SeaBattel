from point import Point #импорт класса точки
#создаэм класс корабля по заданим в работе критериям - lenght длина, nose_point точка начала корабля, place направление
class Ship():
    def __init__(self, lenght, nose_point, place): # 0Horizont, 1 vertical
        self.lenght = lenght
        self.nose_point = nose_point
        self.place = place
        self.life = lenght
    @property # метод что будет создавать корабль и заносить в список
    def make_ship(self):
        ships = []
        for i in range(self.lenght):
            p_x = self.nose_point.x
            p_y = self.nose_point.y
            if self.place == 0:
                p_x += i
            elif self.place == 1:
                p_y += i
            ships.append(Point(p_x, p_y))
        return ships

    def shooten(self, shot):
        return shot in self.make_ship



