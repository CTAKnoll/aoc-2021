from numpy import zeros
from math import floor

class BingoBoard:
    board = zeros((5,5))
    checked = set()

    def flat_board(self, num): 
        return self.board[floor(num/5)][num%5]

    def __init__(self, vals):
        for i in range(0, len(vals)):
            self.board[floor(i/5)][i%5] = vals[i]

    def mark_board(self, num):
        for i in range(25):
            if self.flat_board(i) == num:
                self.checked.add(i)
        return self.check_board()

    def check_board(self):
        return self.horizontal_check(0) or \
        self.horizontal_check(5) or \
        self.horizontal_check(10) or \
        self.horizontal_check(15) or \
        self.horizontal_check(20) or \
        self.vertical_check(0) or \
        self.vertical_check(1) or \
        self.vertical_check(2) or \
        self.vertical_check(3) or \
        self.vertical_check(4)

    def horizontal_check(self, num):
        start = num - num%5
        return all(elem in self.checked for elem in [x for x in range(start, start+5)])
   
    def vertical_check(self, num):
        start = num%5
        return all(elem in self.checked for elem in [x for x in range(start, 25)[::5]])
    
    def sum_unmarked(self):
        sum = 0
        print(self.checked)
        for i in range(25):
            if i not in self.checked:
                sum = sum + self.flat_board(i)
        return sum
        
readings = []
boards = []

def play_bingo():
    for reading in readings:
        for board in boards:
            if(board.mark_board(reading)):
                return board, reading

with open('input.txt') as f:
    content = f.read().split("\n\n")
    readings = list(map(int, content[0].split(",")))
    for i in range(1, len(content)):
        boards.append(BingoBoard(content[i].split()))

marked_board, marked_reading = play_bingo()
print(marked_board.board)
print(marked_reading)
print(marked_board.sum_unmarked())

