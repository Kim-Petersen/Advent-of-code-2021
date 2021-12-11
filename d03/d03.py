from sys import argv
from collections import Counter

def transpose_list_of_list(iterable):
    return list(map(list, zip(*iterable)))

def get_gamma_rate(diagnostic_report):
    gamma_rate = ''
    for column in transpose_list_of_list(diagnostic_report):
        count = Counter(column)
        gamma_rate += max(count, key=count.get)
    return int(gamma_rate,2)

def get_epsilon_rate(diagnostic_report):
    epsilon_rate = ''
    for column in transpose_list_of_list(diagnostic_report):
        count = Counter(column)
        epsilon_rate += min(count, key=count.get)
    return int(epsilon_rate,2)

def oxygen_rate(diagnostic_report, bit_position=0):
    if len(diagnostic_report) == 1:
        return int(diagnostic_report[0],2)
    
    count = Counter(transpose_list_of_list(diagnostic_report)[bit_position])
    if count['1'] == count['0'] or max(count, key=count.get) == '1':
        diagnostic_report = list(filter(lambda x: x[bit_position] == '1', diagnostic_report))
    elif max(count, key=count.get) == '0':       
        diagnostic_report = list(filter(lambda x: x[bit_position] == '0', diagnostic_report))
    bit_position += 1
    return oxygen_rate(diagnostic_report, bit_position)

def co2_scrubber_rate(diagnostic_report, bit_position=0):
    if len(diagnostic_report) == 1:
        return int(diagnostic_report[0],2)
    
    count = Counter(transpose_list_of_list(diagnostic_report)[bit_position])
    if count['0'] == count['1'] or min(count, key=count.get) == '0':
        diagnostic_report = list(filter(lambda x: x[bit_position] == '0', diagnostic_report))
    elif min(count, key=count.get) == '1':       
        diagnostic_report = list(filter(lambda x: x[bit_position] == '1', diagnostic_report))
    bit_position += 1
    return co2_scrubber_rate(diagnostic_report, bit_position)

def main():
    with open(argv[-1], 'r') as f:
        diagnostic_report = f.read().split()

    print(get_gamma_rate(diagnostic_report) * get_epsilon_rate(diagnostic_report))
    print(oxygen_rate(diagnostic_report) * co2_scrubber_rate(diagnostic_report))

if __name__ == '__main__':
    main()