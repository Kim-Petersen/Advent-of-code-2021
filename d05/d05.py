from sys import argv
import re
from itertools import chain
from collections import Counter

def straight_line(line):
    if line['y1'] == line['y2'] or line['x1'] == line['x2']:
        return True
    return False

def points_in_straight_line(line):
    if line['y1'] == line['y2'] and line['x1'] < line['x2']:
        return [(x, line['y1']) for x in range(line['x1'], line['x2']+1)]
    elif line['y1'] == line['y2'] and line['x1'] > line['x2']:
        return [(x, line['y1']) for x in range(line['x2'], line['x1']+1)]
    
    if line['x1'] == line['x2'] and line['y1'] < line['y2']:
        return [(line['x1'], y) for y in range(line['y1'], line['y2']+1)]
    elif line['x1'] == line['x2'] and line['y1'] > line['y2']:
        return [(line['x1'], y) for y in range(line['y2'], line['y1']+1)]

if __name__ == '__main__':
    with open(argv[-1], 'r') as f:
        hydrothermal_vents = f.read().split('\n')

    hydrothermal_vents = [[int(j) for j in re.split(',| -> ', i)] for i in hydrothermal_vents]
    hydrothermal_vents = [{'x1': i, 'y1': j, 'x2': k, 'y2': l} for i,j,k,l in hydrothermal_vents]

    straight_hydrothermal_vents = list(filter(straight_line, hydrothermal_vents))
    
    points = []

    for hydrothermal_vent in straight_hydrothermal_vents:
        points.append(points_in_straight_line(hydrothermal_vent))

    points = list(chain(*points))

    overlaps_at_least_twice = list(filter(lambda x: x[1] > 1, Counter(points).most_common()))

    print(len(overlaps_at_least_twice))
