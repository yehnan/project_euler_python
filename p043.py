

# Problem 43: Sub-string divisibility
# https://projecteuler.net/problem=43

def is_ssd(ns):
    divs = (2, 3, 5, 7, 11, 13, 17)
    shift = 1
    for i in range(0, len(divs)):
        n_sub = int(ns[i+shift:i+shift+3])
        if n_sub % divs[i] != 0:
            return False
    return True

from itertools import permutations as perm

def ssd_bf():
    result = 0
    for np in perm('0123456789'):
        if np[0] == '0':
            continue
        ns = ''.join(np)
        if is_ssd(ns):
            result += int(ns)
    return result
    
def ssd():
    result = 0
    for np in perm('0134'):
        if np[0] == '0':
            continue
        ns = ''.join(np) + '952867'
        if is_ssd(ns):
            result += int(ns)
    for np in perm('0146'):
        if np[0] == '0':
            continue
        ns = ''.join(np) + '357289'
        if is_ssd(ns):
            result += int(ns)
            
    return result
 
#
def test():
    if (is_ssd(str(1406357289)) and 
        is_ssd(str(4106357289)) and 
        not is_ssd(str(4103657289))):
        return 'Pass'
    else:
        return 'Fail'

def main():
    return ssd()

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

