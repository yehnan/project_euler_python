

# Problem 12: Highly divisible triangular number
# https://projecteuler.net/problem=12

# not very fast

def triangle_number_gf():
    n = 0
    i = 1
    while True:
        n += i
        i += 1
        yield n
triangle_number = triangle_number_gf()

def divisors_count(n):
    result = 2
    upper = n // 2
    i = 2
    while i < upper:
        if n % i == 0:
            upper = n // i
            result += 2
        i += 1
    return result

for n in triangle_number:
    if divisors_count(n) > 500:
        print(n)
        break



