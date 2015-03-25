

# Problem 46: Goldbach's other conjecture
# https://projecteuler.net/problem=46

def goc():
    n = 5
    flag = +1
    primes = set([2, 3])
    
    while True:
        if all(n%p!=0 for p in primes):
            primes.add(n)
        else:
            if not any((n - 2*i*i) in primes for i in range(1, n)):
                return n
        n += 3-flag
        flag = -flag

#
def test():
    return 'No test'

def main():
    return goc()

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

