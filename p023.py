

# Problem 23: Non-abundant sums
# https://projecteuler.net/problem=23

from math import sqrt

# proper divisors. includes 1, excludes n itself
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
    
def sum_divisors(n):
    return sum(divisors(n))
    
def is_perfect(n):
    return sum_divisors(n) == n
def is_deficient(n):
    return sum_divisors(n) < n
def is_abundant(n):
    return sum_divisors(n) > n

def abundants(n):
    li = []
    for i in range(1, n+1):
        if is_abundant(i):
            li.append(i)
    return li

def nas():
    abn = set()
    result = 0
    for n in range(1, 28123):
        if is_abundant(n):
            abn.add(n)
        if not any((n-a in abn) for a in abn):
            result += n
    return result
#
def test():
    if is_perfect(28) and is_abundant(12) and sum_divisors(12) == 16:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return nas()
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

