

# Problem 25: 1000-digit Fibonacci number
# https://projecteuler.net/problem=25

memo = {0: 0, 1: 1}
def fib_m(n):
    if n not in memo: 
        memo[n] = fib_m(n-1) + fib_m(n-2) 
    return memo[n]

def main(n):
    i = 1
    while True:
        fn = fib_m(i)
        if len(str(fn)) >= n:
            return i
        i += 1

print(main(3))
print(main(1000))

