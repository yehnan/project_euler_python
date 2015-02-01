

# Problem 9: Special Pythagorean triplet
# https://projecteuler.net/problem=9

#
def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

# given n, generate triplet a < b < c and a + b + c = n
def gen_abc_gf(n):
    for c in range(n//3, n):
        for b in range((n-c)//2, n-c):
            a = n - c - b
            if a < b < c:
                yield a, b, c
                
def main(n):
    gen_abc = gen_abc_gf(n)
    for a, b, c in gen_abc:
        if is_pythagorean_triplet(a, b, c):
            return a*b*c

print(main(1000))
