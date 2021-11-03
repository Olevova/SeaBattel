#создаем классы исключений для их отловов по игре
class BoardException(Exception):
    pass
class BoardOutException(BoardException):
    def __str__(self):
        return "You shoot out of the board,maybe this game not for you"
class BoardBusyException(BoardException):
    def __str__(self):
        return "This cell is not free"
class BoardShipException(BoardException):
    def __str__(self):
        return "This cell is not free"
