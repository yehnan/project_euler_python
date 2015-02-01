

# Problem 2: Even Fibonacci numbers
# https://projecteuler.net/problem=2

# 
memo = {0: 0, 1: 1}
def fib(n):
    if n not in memo: 
        memo[n] = fib(n-1) + fib(n-2) 
    return memo[n]
    
def main(max):
    result = 0
    i = 1
    fn = fib(i)
    while fn <= max:
        if fn % 2 == 0:
            result += fn
        i += 1
        fn = fib(i)
    return result

print(main(4 * 1000 * 1000))


