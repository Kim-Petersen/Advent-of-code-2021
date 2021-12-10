from sys import argv
from itertools import chain

def mark_boards(draw, boards):
    return [[[-1 if draw == num else num for num in row] for row in board] for board in boards]

def winning_board(board):
    for row in board:
        if set(row) == set([-1]):
            return True
    for column in list(zip(*board)):
        if set(column) == set([-1]):
            return True
    return False

if __name__ == '__main__':
    with open(argv[-1], 'r') as f:
        numbers = [int(number) for number in f.readline().split(',')]

        boards = f.read().split('\n\n')
        boards = [board.split('\n') for board in boards]
        boards = [[[int(k) for k in j.split()] for j in i] for i in boards]

        
    for draw in numbers:
        boards = mark_boards(draw, boards)
        
        for board in boards:
            if winning_board(board):
                print(draw * sum(x for x in chain(*board) if x > 0))
                break
        else:
            continue
        break
    



        

                    
                        
    
