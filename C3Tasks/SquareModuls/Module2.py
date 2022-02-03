from Module1 import *

radius = int(input('Input radius of circle: '))
side = int(input('Input side of square: '))

sqrt = SqrtSquare(side)
circle = CircleSquare(radius)

if sqrt > circle:
    print(f'Sqrt is bigger. Square is {sqrt}')
elif circle > sqrt:
    print(f'Circle is bigger. Square is {circle}')
else:
    print(f'Equally. {sqrt} == {circle}')