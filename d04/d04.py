from sys import argv
from itertools import chain

def mark_bingo_boards(draw, bingo_boards):
    return [[[-1 if draw == num else num for num in row] for row in bingo_board] for bingo_board in bingo_boards]

def winning_bingo_board(bingo_board):
    for row in bingo_board:
        if set(row) == set([-1]):
            return True
    for column in list(zip(*bingo_board)):
        if set(column) == set([-1]):
            return True
    return False

def bingo_board_score(bingo_board):
    return sum(x for x in chain(*bingo_board) if x > 0)

if __name__ == '__main__':
    with open(argv[-1], 'r') as f:
        numbers = [int(number) for number in f.readline().split(',')]

        bingo_boards = f.read().split('\n\n')
        bingo_boards = [board.split('\n') for board in bingo_boards]
        bingo_boards = [[[int(k) for k in j.split()] for j in i] for i in bingo_boards]

        scores_times_draw = []
    for draw in numbers:
        bingo_boards = mark_bingo_boards(draw, bingo_boards)
        
        for bingo_board in bingo_boards:
            if winning_bingo_board(bingo_board):
                scores_times_draw.append(draw * bingo_board_score(bingo_board))
                bingo_boards.remove(bingo_board)
        else:
            continue
        break
    print(scores_times_draw[0])
    print(scores_times_draw[-1])
    



        

                    
                        
    
