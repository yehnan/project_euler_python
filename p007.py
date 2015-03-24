

# Problem 7: 10001st prime
# https://projecteuler.net/problem=7

#
def is_prime(n):
    if n % 2 == 0: 
        return False
        
    p = 3
    n_sqrt = n**0.5 + 1
    while p < n_sqrt:
        if n % p == 0: 
            return False
        p += 2
    return True

def nth_prime(n):
    prime = 2
    count = 1
    p_next = 3
    while count < n:
        if is_prime(p_next):
            prime = p_next
            count += 1
        p_next += 2
    return prime

#
def test():
    if nth_prime(6) == 13:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return nth_prime(10001)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

