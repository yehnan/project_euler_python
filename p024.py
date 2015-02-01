

# Problem 24: Lexicographic permutations
# https://projecteuler.net/problem=24

# is this cheat?

from itertools import permutations
p = permutations

print(list(p('012')))

def main():
    for i, x in enumerate(p('0123456789')):
        if i == 10**6-1:
            return ''.join(x)

print(main())

