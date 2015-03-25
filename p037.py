

# Problem 37: Truncatable primes
# https://projecteuler.net/problem=37

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

def is_truncatable_left(n):
    s = str(n)
    s_len = len(s)
    for i in range(1, s_len):
        x = s[i:]
        if not is_prime(int(x)):
            return False
    return True
        
def is_truncatable_right(n):
    s = str(n)
    s_len = len(s)
    for i in range(1, s_len):
        x = s[:-i]
        if not is_prime(int(x)):
            return False
    return True

def check_all(n):
    return is_prime(n) and is_truncatable_left(n) and is_truncatable_right(n)
    
import itertools

def tp(cnt_max):
    result = 0
    cnt = 0
    for n in itertools.count(10):
        if check_all(n):
            result += n
            cnt += 1
            if cnt == cnt_max:
                break
    return result
    
#
def test():
    if check_all(3797):
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return tp(11)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

