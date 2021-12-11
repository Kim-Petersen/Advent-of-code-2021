from sys import _current_frames, argv
from itertools import chain
from collections import Counter

def simulate_lanternfishes_naive(lanternfishes, current_generation, final_generation):
    
    if current_generation == final_generation:
        return lanternfishes
    else:
        lanternfishes = [i-1 for i in lanternfishes]
        lanternfishes = list(chain(lanternfishes, lanternfishes.count(-1) * [8]))
        lanternfishes = [i if i != -1 else 6 for i in lanternfishes]
        return simulate_lanternfishes_naive(lanternfishes, current_generation + 1, final_generation)

def simulate_lanternfishes(lanternfishes, generations):
    timers = Counter({timer: 0 for timer in range(10)})
    lanternfishes = Counter(lanternfishes)
    lanternfishes.update(timers)

    for generation in range(generations):
        lanternfishes[7] += lanternfishes.get(0)
        lanternfishes[9] += lanternfishes.get(0)
        lanternfishes = {lanternfish: lanternfishes.get(lanternfish + 1, 0) for lanternfish in lanternfishes}

    return lanternfishes

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lanternfishes = f.read().split(',')
        lanternfishes = [int(i) for i in lanternfishes]

    
    #print(len(simulate_lanternfishes_naive(lanternfishes,0,80)))
    print(sum(simulate_lanternfishes(lanternfishes, 80).values()))
    print(sum(simulate_lanternfishes(lanternfishes, 256).values()))

    