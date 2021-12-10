from sys import argv
import re
from itertools import chain
from collections import Counter

def straight_line(line):
    if line['y1'] == line['y2'] or line['x1'] == line['x2']:
        return True
    return False

def points_in_line(line):
    x1 = line['x1']
    x2 = line['x2']
    y1 = line['y1']
    y2 = line['y2']
    # right
    if y1 == y2 and x1 < x2:
        return [(x, y1) for x in range(x1, x2+1)]
    # left
    if y1 == y2 and x1 > x2:
        return [(x, y1) for x in range(x2, x1+1)]
    # up
    if x1 == x2 and y1 < y2:
        return [(x1, y) for y in range(y1, y2+1)]
    # down
    if x1 == x2 and y1 > y2:
        return [(x1, y) for y in range(y2, y1+1)]
    # diagonal up-right
    if x1 < x2 and y1 < y2:
        return [(x,y) for x,y in zip(range(x1,x2+1), range(y1,y2+1))]
    # diagonal down-right
    if x1 < x2 and y1 > y2:
        return [(x,y) for x,y in zip(range(x1,x2+1), range(y1,y2-1,-1))]
    # diagonal down-left
    if x1 > x2 and y1 > y2:
        return [(x,y) for x,y in zip(range(x1,x2-1,-1), range(y1,y2-1,-1))]
    # diagonal up-left
    if x1 > x2 and y1 < y2:
        return [(x,y) for x,y in zip(range(x1,x2-1,-1), range(y1,y2+1))]

if __name__ == '__main__':
    with open(argv[-1], 'r') as f:
        hydrothermal_vents = f.read().split('\n')

    hydrothermal_vents = [[int(j) for j in re.split(',| -> ', i)] for i in hydrothermal_vents]
    hydrothermal_vents = [{'x1': i, 'y1': j, 'x2': k, 'y2': l} for i,j,k,l in hydrothermal_vents]

    straight_hydrothermal_vents = list(filter(straight_line, hydrothermal_vents))
    
    points = []

    for hydrothermal_vent in straight_hydrothermal_vents:
        points.append(points_in_line(hydrothermal_vent))

    points = list(chain(*points))

    overlaps_at_least_twice = list(filter(lambda x: x[1] > 1, Counter(points).most_common()))

    print(len(overlaps_at_least_twice))

    points = []

    for hydrothermal_vent in hydrothermal_vents:
        points.append(points_in_line(hydrothermal_vent))

    points = list(chain(*points))

    overlaps_at_least_twice = list(filter(lambda x: x[1] > 1, Counter(points).most_common()))

    print(len(overlaps_at_least_twice))
    