

# Problem 14: Longest Collatz sequence
# https://projecteuler.net/problem=14

memo = {1: 1}
def collatz(n):
    if n not in memo:
        if n % 2 == 0:
            memo[n] = 1 + collatz(n // 2)
        else:
            memo[n] = 1 + collatz(3 * n + 1)
    return memo[n]

n, m = max(((n, collatz(n)) for n in range(2, 1000 * 1000  + 1)), key=lambda x: x[1])
print(n)



