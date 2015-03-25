

# Problem 30: Digit fifth powers
# https://projecteuler.net/problem=30

def limit(power):
    w = 2
    while True:
        num_lower = 10 ** (w - 1)
        sop_upper = (9**power) * w
        if num_lower > sop_upper:
            return sop_upper
        w += 1

def is_sop(n, power):
    sop = sum(int(c)**power for c in str(n))
    return n == sop

def dfp(power):
    result = 0
    for n in range(2, limit(power)+1):
        if is_sop(n, power):
            result += n
    return result

#
def test():
    if dfp(4) == 19316:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return dfp(5)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

