Pi = 3.14

def CircleSquare(radius):
    return (radius ** 2) * Pi

def SqrtSquare(side):
    return side ** 2

if __name__ == '__main__':
    assert CircleSquare(5) == 78.5
    assert SqrtSquare(10) == 100