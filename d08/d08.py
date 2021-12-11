from sys import argv
import re
from collections import Counter
from itertools import chain

def main():
    with open(argv[1], 'r') as f:
        notes = f.read().split('\n')
    
    notes = [[j for j in re.split(' \| |\s', line)] for line in notes]
    notes = [{'sig_pat': line[:-4], 'out_val': line[-4:]} for line in notes]

    out_vals = list(chain(*[line['out_val'] for line in notes]))
    out_vals = list(map(len, out_vals))

    count = Counter(out_vals)

    unique_segment_counts = [count[2], count[3], count[4], count[7]]
    print(sum(unique_segment_counts))

    return None

if __name__ == '__main__':
    main()