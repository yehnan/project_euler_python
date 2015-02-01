

# Problem 1: Multiples of 3 and 5
# https://projecteuler.net/problem=1

# 
def sm35(n):
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result
print(sm35(1000))

# 
def sm35_2(n):
    return sum(i for i in range(1, n) if i%3==0 or i%5==0)
print(sm35_2(1000))

#
def sm35_3(n):
    sm3 = sum(range(3, n, 3))
    sm5 = sum(range(5, n, 5))
    sm15 = sum(range(3*5, n, 3*5))
    return sm3 + sm5 - sm15
print(sm35_3(1000))

#
def sm35_4(n):
    def sub(n):
        a, b = 3, 5
        while a < n or b < n:
            if a < b:
                yield a
                a += 3
            elif a == b:
                yield a
                a += 3
                b += 5
            elif a > b:
                yield b
                b += 5
    return sum(sub(n))
print(sm35_4(1000))


