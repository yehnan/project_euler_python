

# Problem 5: Smallest multiple
# https://projecteuler.net/problem=5

def gcd(a, b): # greatest common divisor
    while b:
        a, b = b, a%b
    return a

def lcm(a, b): # least common multiple
    return a * b / gcd(a, b)

def main(x, y):
    m = 1
    for n in range(x, y+1):
        m = lcm(m, n)
    return m

print(main(1, 10))
print(main(1, 20))

