

# Problem 38: Pandigital multiples
# https://projecteuler.net/problem=38

def is_pandigital(num):
    ds = '123456789'
    s = str(num)
    ins = sum(1 for d in ds if d in s)
    return ins == len(ds)
            
def prod(num):
    s = str(num)
    n = 2
    while True:
        s += str(num * n)
        if len(s) == 9:
            return s, n
        elif len(s) > 9:
            return False, False
        n += 1
    return False, False

def pm():
    num_max = 0
    for i in range(1, 4+1):
        for num in range(10**(i-1), 10**i - 1):
            s, n = prod(num)
            if s and is_pandigital(s) and int(s) > num_max:
                num_max = int(s)
    return num_max

#
def test():
    if prod(192) == ('192384576', 3) and prod(9) == ('918273645', 5):
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return pm()

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

