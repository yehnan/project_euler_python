

# Problem 15: Lattice paths
# https://projecteuler.net/problem=15

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
    
def lp(row, col):
    return factorial(row+col) // factorial(row) // factorial(col)

#
def test():
    if lp(2, 2) == 6:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return lp(20, 20)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

