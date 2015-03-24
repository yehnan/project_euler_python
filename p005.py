

# Problem 5: Smallest multiple
# https://projecteuler.net/problem=5

def gcd(a, b): # greatest common divisor
    while b:
        a, b = b, a%b
    return a

def lcm(a, b): # least common multiple
    return a * b // gcd(a, b)

def sm(x, y):
    m = 1
    for n in range(x, y+1):
        m = lcm(m, n)
    return m

#
def test():
    if sm(1, 10) == 2520:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return sm(1, 20)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

