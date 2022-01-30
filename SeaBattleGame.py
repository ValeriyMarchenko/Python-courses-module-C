from shutil import ExecError
from random import randint
from timeit import repeat
from tkinter import N

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return 'Out of board'

class BoardUsedException(BoardException):
    def __str__(self):
        return 'You have already shot this cell'

class BoardWrongShipException(BoardException):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'

class Ship:
    def __init__(self, length, head, direction, hp):
        self.length = length
        self.head = head
        self.direction = direction
        self.hp = hp

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            cur_x = self.head.x
            cur_y = self.head.y

            if self.direction == 0:
                cur_x += i
            elif self.direction == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid = False, size = 6):
        self.size = size
        self.hid = hid
        self.count = 0
        self.field = [['0'] * size for _ in range(size)]
        self.busy = []
        self.ships = []
    
    def __str__(self):
        res = ''
        res += '  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            res += f'\n{i + 1} | ' + ' | '.join(row) + ' | ' 
        
        if self.hid:
            res = res.replace('∎', '0')
        return res

    def out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def contour(self, ship, verb = 0):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1), 
            (1, -1), (1, 0), (1, 1)
        ]

        for dot in ship.dots:
            for dx, dy in near:
                cur = Dot(dot.x + dx, dot.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = '.'
                    self.busy.append(cur)

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
        for dot in ship.dots:
            self.field[dot.x][dot.y] = '∎'
            self.busy.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException()
        
        if dot in self.busy:
            raise BoardUsedException()
        
        self.busy.append(dot)
        
        for ship in self.ships:
            if dot in ship.dots:
                ship.hp -= 1
                self.field[dot.x][dot.y] = "X"
                if ship.hp == 0:
                    self.count += 1
                    self.contour(ship, verb = True)
                    print("Ship is eliminated")
                    return False
                else:
                    print("Ship is stricken")
                    return True
        
        self.field[dot.x][dot.y] = "."
        print("Miss")
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy
    
    def ask(self):
        raise NotImplementedError()
    
    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        dot = Dot(randint(0, 5), randint(0, 5))
        print(f"AI turn: {dot.x + 1} {dot.y + 1}")
        return dot

class User(Player):
    def ask(self):
        while True:
            coords = input("    Input x and y: ").split() 

            if len(coords) != 2:
                print()
                print("You need two coords to make a move")
                print()
                continue

            x, y = coords
        
            if not (x.isdigit() and y.isdigit()):
                print()
                print("Input numbers instead of mess")
                print()
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)

class Game:
    def __init__(self, size = 6):
        self.size = size 
        self.ship_length = [3, 2, 2, 1, 1, 1, 1]
        players_board = self.rand_board()
        ai_board  = self.rand_board()
        ai_board.hid = False

        self.ai = AI(ai_board, players_board)
        self.player = User(players_board, ai_board)

    def start(self):
        print()
        print('----------------------')
        print('    Sea Battle Game   ')
        print('----------------------')
        print('     How to play:     ')
        print('  x - number of str   ')
        print(' y - number of column ')
        print()

    def rand_generation(self):
        board = Board(size = self.size)
        attempts = 0
        for i in self.ship_length:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(i, Dot(randint(0, self.size), randint(0, self.size)), randint(0, 1), i)
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def rand_board(self):
        board = None
        while board is None:
            board = self.rand_generation()
        return board

    @staticmethod
    def two_fields(first_field, second_field):
        first_field = first_field.split("\n")
        second_field = second_field.split("\n")
        maxlen = max(map(len, first_field))
        result = ""
        for line1, line2 in zip(first_field, second_field):
            result += f"{line1:{maxlen}}    |    {line2}\n"
        return result

    def print_boards(self):
        print('-' * 70)
        print('Players board:')
        print(self.player.board)
        print('-' * 16)
        print('Computers board:')
        print(self.ai.board)

    def game_loop(self):
        turn = 0
        while True:
            players_out = "Players board:\n\n" + str(self.player.board)
            ai_out = "Computers board:\n\n" + str(self.ai.board)
            print("-" * 64)
            print(Game.two_fields(players_out, ai_out))

            if turn % 2 == 0:
                print('-' * 64)
                print('Players turn')
                repeat = self.player.move()
            else:
                print('-' * 64)
                print('Computers turn')
                repeat = self.ai.move()

            if repeat:
                turn -= 1

            if  self.ai.board.defeat():
                self.print_boards()
                print('-' * 64)
                print('Player win')
                break

            if self.player.board.defeat():
                self.print_boards()
                print('-' * 64)
                print('Computer win')
                break
            
            turn += 1

    def game_start(self):
        self.start()
        self.game_loop()
        

g = Game()
g.game_start()