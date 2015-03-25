

# Problem 36: Double-base palindromes
# https://projecteuler.net/problem=36

def is_palindrome_10(n):
    s = str(n)
    return s == ''.join(reversed(s))
    
def is_palindrome_2(n):
    s = bin(n)[2:]
    return s == ''.join(reversed(s))
    
def is_palindrome(n):
    return is_palindrome_10(n) and is_palindrome_2(n)
    
def dbp(max):
    return sum(i for i in range(1, max) if is_palindrome(i))

#
def test():
    if is_palindrome(585):
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return dbp(1 * 1000 * 1000)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

