

# Problem 40: Champernowne's constant
# https://projecteuler.net/problem=40


def d(digits):
    li = []
    i = 1
    n = 0
    while True:
        s = str(i)
        li.append(s)
        n += len(s)
        if n > digits:
            break
        i += 1
    return ''.join(li)
    
def main(pow):
    s = d(10**pow)
    result = 1
    for i in range(pow):
        result *= int(s[10**i-1])
    return result

print(main(6))




