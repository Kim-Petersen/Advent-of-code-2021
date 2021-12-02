from sys import argv

if __name__ == '__main__':
    try:
        with open(argv[-1], 'r') as f:
            commands = f.read().split('\n')
            commands = [x.split() for x in commands]

        # Part one   
        position_horizontal = 0
        position_depth = 0
        
        for instruction, magnitude in commands:
            if instruction == 'forward':
                position_horizontal += int(magnitude)
            if instruction == 'down':
                position_depth += int(magnitude)
            if instruction == 'up':
                position_depth -= int(magnitude)

        print(position_horizontal * position_depth)

        # Part two
        position_horizontal = 0
        position_depth = 0
        aim = 0

        for instruction, magnitude in commands:
            if instruction == 'forward':
                position_horizontal += int(magnitude)
                position_depth += aim * int(magnitude)
            if instruction == 'down':
                aim += int(magnitude)
            if instruction == 'up':
                aim -= int(magnitude)

        print(position_horizontal * position_depth)
    except:
        print(argv[0])