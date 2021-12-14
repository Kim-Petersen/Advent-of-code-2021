from sys import argv
import re
from collections import Counter
from itertools import chain

def interpret_sig_pat(note):
    sig_pattern = sorted(note['sig_pat'],key=len)
    
    # Digit lengths
    # 1 = 2 seg

    # 7 = 3 seg
    
    # 4 = 4 seg
    
    # 2 = 5 seg
    # 3 = 5 seg
    # 5 = 5 seg
    
    # 0 = 6 seg
    # 6 = 6 seg
    # 9 = 6 seg

    # 8 = 7 seg

    digits = {
        '1': set(sig_pattern[0]),
        '7': set(sig_pattern[1]),
        '4': set(sig_pattern[2]),
        '8': set(sig_pattern[9])
    }

    for i in sig_pattern[6:9]:
        if (digits['7'] | digits['4']) < set(i):
            digits['9'] = set(i)

    for i in sig_pattern[3:6]:
        if (digits['4'] - digits['1']) < set(i):
            digits['5'] = set(i)
    
    for i in sig_pattern[3:6]:
        if (digits['8'] - digits['5']) < set(i):
            digits['2'] = set(i)
    
    for i in sig_pattern[3:6]:
        if len(set(i) - digits['1']) == 3:
            digits['3'] = set(i)

    for i in sig_pattern[6:9]:
        if len(set(i) - digits['5']) == 2:
            digits['0'] = set(i)

    for i in sig_pattern[6:9]:
        if len(set(i) - digits['1']) == 5:
            digits['6'] = set(i)

    return digits

def interpret_output_val(note):
    output = note['out_val']
    digits = interpret_sig_pat(note)
    
    output_decoded = ''

    for i in output:
        for digit, signal in digits.items():
            if set(i) == signal:
                output_decoded += digit
    
    return output_decoded

def main():
    with open('d08 input.txt', 'r') as f:
        notes = f.read().split('\n')
    
    notes = [[j for j in re.split(' \| |\s', line)] for line in notes]
    notes = [{'sig_pat': line[:-4], 'out_val': line[-4:]} for line in notes]

    out_vals = list(chain(*[line['out_val'] for line in notes]))
    out_vals = list(map(len, out_vals))

    count = Counter(out_vals)

    unique_segment_counts = [count[2], count[3], count[4], count[7]]
    print(sum(unique_segment_counts))

    digits = [interpret_sig_pat(i) for i in notes]
    out_vals = [int(interpret_output_val(i)) for i in notes]
    print(sum(out_vals))
    

    return None

if __name__ == '__main__':
    main()