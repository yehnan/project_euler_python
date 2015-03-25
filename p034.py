

# Problem 34: Digit factorials
# https://projecteuler.net/problem=34

from math import factorial
facts = [factorial(i) for i in range(10)]

def limit(): # 9999999 is way more than its fact-sum
    n = 2
    while True:
        if 10**(n-1) > facts[9]*n:
            return n
        n += 1

def check(n):
    tmp = n
    total = 0
    while tmp > 0:
        total += facts[tmp % 10]
        tmp //= 10
    return total == n
    
def df():
    result = 0
    for n in range(10, facts[9] * (limit()-1)):
        if check(n):
            result += n
    return result

#
def test():
    if check(145):
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return df()

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

