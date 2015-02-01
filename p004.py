

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

def main(d):
    result = []
    for x in range(10**d-1, 10**(d-1)-1, -1):
        for y in range(10**d-1, 10**(d-1)-1, -1):
            if is_palindrome(x * y):
                result.append((x*y, x, y))
    return result

print(sorted(main(2), key=lambda x: x[0])[-1])
print(sorted(main(3), key=lambda x: x[0])[-1])
