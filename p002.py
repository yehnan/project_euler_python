

# Problem 2: Even Fibonacci numbers
# https://projecteuler.net/problem=2

# 
memo = {0: 0, 1: 1}
def fib(n):
    if n not in memo: 
        memo[n] = fib(n-1) + fib(n-2) 
    return memo[n]
    
def efn(max):
    result = 0
    n = 1
    fn = fib(n)
    while fn <= max:
        if fn % 2 == 0:
            result += fn
        n += 1
        fn = fib(n)
    return result

#
def test():
    print('No test')
    
def main():
    print(efn(4 * 1000 * 1000))

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test()
    else:
        main()

