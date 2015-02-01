

# Problem 43: Sub-string divisibility
# https://projecteuler.net/problem=43

from itertools import permutations

# brute force

def is_ssd(n): # sub-string divisibility
    divs = (2, 3, 5, 7, 11, 13, 17)
    ns = str(n)
    shift = 1
    for i in range(0, len(divs)):
        n_sub = int(ns[i+shift:i+shift+3])
        if n_sub % divs[i]:
            return False
    return True

# print(is_ssd(1406357289))  # True
# print(is_ssd(4106357289))  # True
# print(is_ssd(4103657289))  # False

def main():
    result = 0
    for np in permutations('0123456789'):
        ns = ''.join(np)
        if ns[0] == '0':
            continue
        n = int(ns)
        if is_ssd(n):
            result += n
    return result

print(main())

