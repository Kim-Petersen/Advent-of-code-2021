from sys import argv
from itertools import chain, compress
from types import coroutine

def is_lowpoint(heightmap, x, y):
    neighbours = {}
    point = heightmap[y][x]
    
    if y == 0:
        pass
    else:
        neighbours['up'] = (heightmap[y-1][x])
    
    if x == len(heightmap[y])-1:
        pass
    else:
        neighbours['right'] = heightmap[y][x+1]
    
    if y == len(heightmap)-1:
        pass
    else:
        neighbours['down'] = heightmap[y+1][x]
    
    if x == 0:
        pass
    else:
        neighbours['left'] = heightmap[y][x-1]

    if all([point < i for i in list(neighbours.values())]):
        return True
    else:
        return False

def min_mask(heightmap):
    heightmap_height = len(heightmap)
    heightmap_width = len(heightmap[0])

    return [[is_lowpoint(heightmap, x, y) for x in range(heightmap_width)] for y in range(heightmap_height)]

def main():
    with open(argv[1], 'r') as f:
        heightmap = f.read().split()

    heightmap = [[int(x) for x in c] for c in heightmap]
    
    risk_levels = [x + 1 for x in compress(chain(*heightmap), chain(*min_mask(heightmap)))]
    
    print(sum(risk_levels))

    return None

if __name__ == '__main__':
    main()