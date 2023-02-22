# class for checkers figure and queen
class Figure:
    def __init__(self, color):
        self.color = color
        self.isQueen = False

    def setQueen(self):
        self.isQueen = True

    def getColor(self):
        return self.color

    def getIsQueen(self):
        return self.isQueen

    def __str__(self):
        if self.color == "black":
            if self.isQueen:
                return 4
            else:
                return 2
        elif self.color == "white":
            if self.isQueen:
                return 3
            else:
                return 1

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.color == other.color and self.isQueen == other.isQueen:
            return True
        else:
            return False
