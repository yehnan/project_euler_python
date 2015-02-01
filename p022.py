

# Problem 22: Names scores
# https://projecteuler.net/problem=22

from io import open

def alphabetical_value(s):
    v = 0
    for c in s:
        v += ord(c) - ord('A') + 1
    return v

with open('p022_names.txt', 'r', encoding='ascii') as fin:
    names = sorted(eval(''.join(('[', fin.read(), ']'))))
    scores = 0
    for i, name in enumerate(names):
        scores += alphabetical_value(name) * (i + 1)
    print(scores)











