

# Problem 99: Largest exponential
# https://projecteuler.net/problem=99

from io import open
from math import log

def main(filename):
    be_max_log = 0
    base_max = 0
    exp_max = 0
    line_number_max = 0
    with open(filename, 'r', encoding='ascii') as fin:
        for ln, line in enumerate(fin):
            be = line.split(',')
            base, exp = int(be[0]), int(be[1])
            m = exp * log(base)
            if be_max_log < m:
                be_max_log = m
                base_max = base
                exp_max = exp
                line_number_max = ln + 1
    return line_number_max

print(main('p099_base_exp.txt'))

