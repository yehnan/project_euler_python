

# Problem 16: Power digit sum
# https://projecteuler.net/problem=16

def pds(n):
    num = 2 ** n
    result = 0
    for d in str(num):
        result += int(d)
    return result

#
def test():
    if pds(15) == 26:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return pds(1000)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

