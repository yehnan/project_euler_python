

# Problem 13: Large sum
# https://projecteuler.net/problem=13

from io import open

def ls(filename):
    with open(filename, 'r', encoding='ascii') as fin:
        total = sum(int(line) for line in fin)
        return str(total)[:10]

#
def test():
    return 'No test'
    
def main():
    return ls('p013_data.txt')
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

