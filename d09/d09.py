from sys import argv

def find_neighbours(heightmap, x, y):
    neighbours = {}
    if y == 0:
        pass
    else:
        neighbours['up'] = (heightmap[y-1][x], (x,y-1))
    
    if x == len(heightmap[y])-1:
        pass
    else:
        neighbours['right'] = (heightmap[y][x+1], (x+1,y))
    
    if y == len(heightmap)-1:
        pass
    else:
        neighbours['down'] = (heightmap[y+1][x], (x,y+1))
    
    if x == 0:
        pass
    else:
        neighbours['left'] = (heightmap[y][x-1], (x-1,y))
    
    return neighbours

def is_lowpoint(heightmap, x, y):
    neighbours = find_neighbours(heightmap, x, y)
    
    if all([heightmap[y][x] < i[0] for i in neighbours.values()]):
        return True
    else:
        return False

def find_basins(heightmap):
    min_coordinates = [(x, y) for x in range(100) for y in range(100) if is_lowpoint(heightmap, x, y)]




def main():
    with open(argv[1], 'r') as f:
        heightmap = f.read().split()

    heightmap = [[int(x) for x in c] for c in heightmap]
    
    min_coordinates = [(x, y) for x in range(100) for y in range(100) if is_lowpoint(heightmap, x, y)]

    risk_levels = [heightmap[y][x] + 1 for x,y in min_coordinates]

    print(sum(risk_levels))

    return None

if __name__ == '__main__':
    main()