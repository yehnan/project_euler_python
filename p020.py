

# Problem 20: Factorial digit sum
# https://projecteuler.net/problem=20

def fact(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

def fds(n):
    s = str(fact(n))
    result = 0
    for c in s:
        result += int(c)
    return result

#
def test():
    if fds(10) == 27:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return fds(100)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

