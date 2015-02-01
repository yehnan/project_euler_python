

# Problem 23: Non-abundant sums
# https://projecteuler.net/problem=23

# ok-ish, not very fast

from math import sqrt

# includes 1, excludes n itself
def divisors(n):
    result = [1]
    result_2 = []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            x = n // i
            if x != i:
                result_2.insert(0, n//i)
    result.extend(result_2)
    return result
def sod(n): # sum of divisors
    return sum(divisors(n))
    
# print(divisors(4), sod(4))    # [1, 2]                      3     note: not [1, 2, 2]
# print(divisors(12), sod(12))   # [1, 2, 3, 4, 6]            16  smallest abundant 
# print(divisors(24), sod(24))   # [1, 2, 3, 4, 6, 8, 12]     36
# print(divisors(28), sod(28))   # [1, 2, 4, 7, 14]           28  perfect
# print(divisors(30), sod(30))   # [1, 2, 3, 5, 6, 10, 15]    42
# print(divisors(28123), sod(28123))   # [1]    prime

def is_perfect(n):
    return sod(n) == n
def is_deficient(n):
    return sod(n) < n
def is_abundant(n):
    return sod(n) > n

def abundants(n):
    li = []
    for i in range(1, n+1):
        if is_abundant(i):
            li.append(i)
    return li

def main(limit):
    answers = set(range(1, limit+1))
    abs = abundants(limit)
    # print(abs)
    for i in abs:
        tmp = set()
        for j in abs:
            tmp.add(i+j)
        # print(tmp)
        answers -= tmp
    # print(answers)
    return sum(answers)

limit = 28123 
print(main(limit))

