

# Problem 22: Names scores
# https://projecteuler.net/problem=22

from io import open

def alphabetical_value(s):
    v = 0
    for c in s:
        v += ord(c) - ord('A') + 1
    return v

def ns(filename):
    with open(filename, 'r', encoding='ascii') as fin:
        names = sorted(eval(''.join(('[', fin.read(), ']'))))
        scores = 0
        for i, name in enumerate(names):
            scores += alphabetical_value(name) * (i + 1)
        return scores

#
def test():
    return 'No test'
    
def main():
    return ns('p022_data.txt')
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

