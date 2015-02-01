

# Problem 34: Digit factorials
# https://projecteuler.net/problem=34

memo = {0: 1, 1: 1, 2: 2}
def fact(n):
    if n not in memo:
        memo[n] = n * fact(n-1)
    return memo[n]
facts = [fact(i) for i in range(10)]

def limit():   # 9999999 is way more than its fact-sum
    n = 2
    while True:
        if 10**(n-1) > facts[9]*n:
            return n
        n += 1
def check_1(n):
    return n == sum(facts[int(i)] for i in str(n))
def check_2(n):
    tmp = n
    total = 0
    while tmp > 0:
        total += facts[tmp % 10]
        tmp //= 10
    return total == n
def main():
    result = 0
    for n in xrange(10, facts[9]*(limit()-1)):
        if check_2(n):
            result += n
    return result

# print(limit())
print(main())

