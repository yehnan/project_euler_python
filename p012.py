

# Problem 12: Highly divisible triangular number
# https://projecteuler.net/problem=12

def divisors_count(n):
    dc = 1
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1
    dc *= (cnt + 1)
    
    p = 3
    while n != 1:
        cnt = 0
        while n % p == 0:
            n //= p
            cnt += 1
        dc *= (cnt + 1)
        p += 2
    return dc
    
def triangle_number_gf():
    tn = 0
    i = 1
    while True:
        tn += i
        i += 1
        yield tn

def hdtn(dc):
    for tn in triangle_number_gf():
        if divisors_count(tn) > dc:
            return tn

#
def test():
    if hdtn(5) == 28 and hdtn(3) == 6:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return hdtn(500)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

