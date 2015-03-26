

# Problem 49: Prime permutations
# https://projecteuler.net/problem=49

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True
    
def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))

def pp(n_from, n_to):
    for n in range(n_from, n_to+1, 2):
        n2, n3 = n+3330, n+6660
        if (is_prime(n) and is_prime(n2) and is_prime(n3) and 
            is_perm(n, n2) and is_perm(n2, n3)):
            return str(n) + str(n2) + str(n3)
            
    return None

#
def test():
    if pp(1001, 1488) == '148748178147':
        return 'Pass'
    else:
        return 'Fail'

def main():
    return pp(1489, 9999)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

