

# Problem 4: Largest palindrome product
# https://projecteuler.net/problem=4

# 
def is_palindrome(n):
    ns = str(n)
    a, b = 0, len(ns)-1
    while a < b:
        if ns[a] != ns[b]:
            return False
        else:
            a += 1
            b -= 1
    return True

def palindromes(d):
    result = []
    # example: if d == 3, 
    # x will be from 999 to 100,
    # y will be from x to 100
    for x in range(10**d-1, 10**(d-1)-1, -1):
        for y in range(x, 10**(d-1)-1, -1):
            if is_palindrome(x * y):
                result.append((x*y, x, y))
    return result

def palindromes_max(d):
    return sorted(palindromes(d), key=lambda x: x[0])[-1][0]

#
def test():
    if palindromes_max(2) == 9009:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return palindromes_max(3)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

