

# Problem 55: Lychrel numbers
# https://projecteuler.net/problem=55

def is_palindrome(n):
    ns = str(n)
    return ns == ns[::-1]
    
def is_lychrel(n, limit=50):
    tmp = n
    for i in range(limit):
        tmp += int(str(tmp)[::-1])
        if is_palindrome(tmp):
            return False
    return True
    
# print(is_lychrel(47))     # False
# print(is_lychrel(349))    # False
# print(is_lychrel(10677, 50))  # True
# print(is_lychrel(10677, 60))  # False
# print(is_lychrel(196))    # True
# print(is_lychrel(4994))   # True


def main(m):
    return sum(1 for n in range(10, m+1) if is_lychrel(n))

print(main(10*1000))

