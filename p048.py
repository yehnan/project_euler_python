

# Problem 48: Self powers
# https://projecteuler.net/problem=48

def sp(n, d=None):
    result = 0
    for i in range(1, n+1):
        result += i ** i
    result = str(result)
    if d is not None:
        result = result[-d:]
    return result

#
def test():
    if sp(10) == '10405071317':
        return 'Pass'
    else:
        return 'Fail'

def main():
    return sp(1000, 10)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

