

# Problem 33: Digit cancelling fractions
# https://projecteuler.net/problem=33

from fractions import gcd

# n: numerator, d: denominator
def is_it(n, d):
    ns = str(n)
    ds = str(d)
    if ns[0] == ds[0]:
        x = int(ns[1])
        y = int(ds[1])
        if (n // gcd(n, d) == x // gcd(x, y) and
           d // gcd(n, d) == y // gcd(x, y)):
           return True
    elif ns[0] == ds[1]:
        x = int(ns[1])
        y = int(ds[0])
        if (n // gcd(n, d) == x // gcd(x, y) and
           d // gcd(n, d) == y // gcd(x, y)):
           return True
    elif ns[1] == ds[0]:
        x = int(ns[0])
        y = int(ds[1])
        if (n // gcd(n, d) == x // gcd(x, y) and
           d // gcd(n, d) == y // gcd(x, y)):
           return True
    return False
    
def is_dd(num): # double digit, like 11, 22...
    return (num // 10) == (num % 10)
    
def is_m10(num): # mutiple of 10, like 10, 20...
    return (num % 10) == 0

def dcf():
    prod_n = 1
    prod_d = 1
    count = 0
    for d in range(10, 99+1):  # two digits
        for n in range(10, d): # less than 1
            if (not is_dd(n) and not is_dd(d) and 
                not is_m10(n) and not is_m10(d) and
                is_it(n, d)):
                prod_n *= n
                prod_d *= d
                count += 1
    gg = gcd(prod_n, prod_d)
    return prod_n//gg, prod_d//gg, count

#
def test():
    if dcf()[2] == 4:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return dcf()[1]

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

