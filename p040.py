

# Problem 40: Champernowne's constant
# https://projecteuler.net/problem=40

def d(dn):
    li = []
    i = 1
    n = 0
    while True:
        s = str(i)
        li.append(s)
        n += len(s)
        if n > dn:
            break
        i += 1
    return ''.join(li)

def cc(pow):
    s = d(10**pow)
    result = 1
    for i in range(pow):
        result *= int(s[10**i-1])
    return result

#
def test():
    if d(20)[12 - 1] == '1':
        return 'Pass'
    else:
        return 'Fail'

def main():
    return cc(7)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())




