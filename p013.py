

# Problem 13: Large sum
# https://projecteuler.net/problem=13

from io import open

with open('p013_numbers.txt', 'r', encoding='ascii') as fin:
    total = sum(int(line) for line in fin)
    print(str(total)[:10])
        


