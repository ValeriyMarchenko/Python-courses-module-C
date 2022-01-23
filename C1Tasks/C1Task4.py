from msilib.schema import Error


class Square:
    _side = None

    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
        else:
            raise ValueError('Side must be > 0')

    @property
    def square(self):
        return self.side ** 2

sq = Square(5)
print(sq.square)