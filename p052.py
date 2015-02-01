

# Problem 52: Permuted multiples
# https://projecteuler.net/problem=52

def same_digits(n1, iterable):
    n1set = set(str(n1))
    for n2 in iterable:
        n2set = set(str(n2))
        if n1set != n2set:
            return False
    return True

# print(same_digits(125874, [251748]))

def main():
    x = 1
    while True:
        if same_digits(x, [x*2, x*3, x*4, x*5, x*6]):
            return x
        x += 1
    return x
print(main()) # 142857



