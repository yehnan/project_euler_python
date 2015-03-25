

# Problem 25: 1000-digit Fibonacci number
# https://projecteuler.net/problem=25

memo = {0: 0, 1: 1}
def fib_m(n):
    if n not in memo: 
        memo[n] = fib_m(n-1) + fib_m(n-2) 
    return memo[n]

def ndfn(nd):
    i = 1
    while True:
        fn = fib_m(i)
        if len(str(fn)) >= nd:
            return i
        i += 1

#
def test():
    if ndfn(3) == 12:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return ndfn(1000)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

