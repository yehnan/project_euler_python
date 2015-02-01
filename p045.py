

# Problem 45: Triangular, pentagonal, and hexagonal
# https://projecteuler.net/problem=45

def gen_n(f):
    i = 1
    while True:
        n = f(i)
        yield n
        i += 1

def sub_gf(fa, fb):
    a = next(fa)
    b = next(fb)
    while True:
        if a < b:
            a = next(fa)
        elif a > b:
            b = next(fb)
        else:
            yield a
            a = next(fa)
def main(n):
    tn = gen_n(lambda i: i * (i+1) // 2)
    pn = gen_n(lambda i: i * (3*i - 1) // 2)
    hn = gen_n(lambda i: i * (2*i - 1))

    sub1 = sub_gf(tn, pn)
    sub2 = sub_gf(sub1, hn)
    result = 0
    for i in range(n):
        result = next(sub2)
    return result
    
# print(main(1))
# print(main(2))
print(main(3))
