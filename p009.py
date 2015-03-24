

# Problem 9: Special Pythagorean triplet
# https://projecteuler.net/problem=9

#
def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

# given n, generate triplet a < b < c and a + b + c = n
def abc_gf(n):
    for c in range(n//3, n):
        for b in range((n-c)//2, n-c):
            a = n - c - b
            if a < b < c:
                yield a, b, c

def spr(n):
    for a, b, c in abc_gf(n):
        if is_pythagorean_triplet(a, b, c):
            return a*b*c

#
def test():
    return 'No test'
    
def main():
    return spr(1000)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

