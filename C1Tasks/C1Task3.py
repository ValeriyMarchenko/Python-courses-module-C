class Square:
    def __init__(self, side):
        self.side = side

class SquareFactory:
    @staticmethod
    def get_side(side):
        return Square(side)

square = SquareFactory.get_side(3)
print(square.side)