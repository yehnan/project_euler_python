

# Problem 36: Double-base palindromes
# https://projecteuler.net/problem=36

def is_palindrome10(n):
    s = str(n)
    return s == ''.join(reversed(s))
def is_palindrome2(n):
    s = bin(n)[2:]
    return s == ''.join(reversed(s))
def is_palindrome(n):
    return is_palindrome10(n) and is_palindrome2(n)
print(is_palindrome(585))

print(sum([i for i in range(1, 1000*1000) if is_palindrome(i)]))


