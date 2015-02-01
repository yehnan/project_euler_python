

# Problem 169: Exploring the number of different ways a number can be expressed as a sum of powers of 2
# https://projecteuler.net/problem=169

def upper_power(n):
    i = 0
    m = 2 ** i
    while m < n:
        i += 1
        m = 2 ** i
    return i-1
memo = {}
def sub(n, k):
    key = str(n)+str(k)
    if key in memo:
        return memo[key]
    if n < 0:
        memo[key] = 0
        return 0
    elif n == 0:
        memo[key] = 1
        return 1
    if k < 0:
        memo[key] = 0
        return 0
    elif k < upper_power(n) - 1:
        memo[key] = 0
        return 0
    else:
        kk = 2 ** k
        result = sub(n, k-1) + sub(n-kk, k-1) + sub(n-kk*2, k-1)
        memo[key] = result
        return result

def main(n):
    return sub(n, upper_power(n))
# print(upper_power(10))
# print(main(10))  # 5
print(main(10**25)) 

