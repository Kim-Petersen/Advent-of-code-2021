from sys import argv
from typing import final

def cost_of_alignment_1(initial_positions, final_position):
    costs = [abs(final_position - i) for i in initial_positions]
    return sum(costs)

def cost_of_alignment_2(initial_positions, final_position):
    fuel_cost = lambda x: int(0.5 * x ** 2 + 0.5 * x)
    costs = [fuel_cost(abs(final_position - i)) for i in initial_positions]
    return sum(costs)

def main():
    with open(argv[1], 'r') as f:
        crab_positions = f.read().split(',')
        crab_positions = list(map(int, crab_positions))
        
        final_positions = {i: cost_of_alignment_1(crab_positions, i) for i in range(min(crab_positions), max(crab_positions)+1)}
        
        print(min(final_positions.values()))

        final_positions = {i: cost_of_alignment_2(crab_positions, i) for i in range(min(crab_positions), max(crab_positions)+1)}

        print(min(final_positions.values()))
    return None

if __name__ == '__main__':
    main()