

# Problem 28: Number spiral diagonals
# https://projecteuler.net/problem=28

def nsd(size):
    result = 1  # center
    for i in range(3, size+2, 2):
        result += i**2   # top-right
        tmp = (i-2)**2 + 1 + i - 2
        result += tmp   # bottom-right
        result += tmp + i - 1   # bottom-left
        tmp = tmp + i - 1
        result += tmp + i - 1   # top-left
    return result

#
def test():
    if nsd(5) == 101:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return nsd(1001)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

