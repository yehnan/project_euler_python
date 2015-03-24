

# Problem 21: Amicable numbers
# https://projecteuler.net/problem=21

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

def amicable(a):
    b = da = sum_divisors(a)
    db = sum_divisors(b)
    if a != b and a == db and b == da:
        return b
    else:
        None

def an(m):
    set_amicable = set()
    for a in range(1, m):
        if a not in set_amicable:
            b = amicable(a)
            if b:
                set_amicable.add(a)
                set_amicable.add(b)
    return sum(set_amicable)

#
def test():
    if sum_divisors(220) == 284 and sum_divisors(284) == 220:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return an(10000)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

