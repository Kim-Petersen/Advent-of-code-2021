from sys import argv
from collections import Counter

if __name__ == '__main__':
    with open(argv[-1], 'r') as f:
        diagnostic_report = f.read().split()
    
    diagnostic_report = [[char for char in word] for word in diagnostic_report]
    diagnostic_report_transposed = list(map(list, zip(*diagnostic_report)))

    # Part one
    gamma_rate = []
    epsilon_rate = []

    for column in diagnostic_report_transposed:
        count = Counter(column).most_common()
        gamma_rate.append(count[0][0])
        epsilon_rate.append(count[1][0])

    gamma_rate = int(''.join(gamma_rate),2)
    epsilon_rate = int(''.join(epsilon_rate),2)

    print(gamma_rate * epsilon_rate)


