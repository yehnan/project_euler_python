

# Problem 142: Perfect Square Collection
# https://projecteuler.net/problem=142

# brute force, take very long time

# from math import sqrt

memo = set()
memo_n_max = 100
for i in range(1, memo_n_max+1):
    memo.add(i**2)
memo_sq_max = max(memo)

def is_psq(x, y, z):
    tests = [x+y, x-y, x+z, x-z, y+z, y-z]
    a, b, c, d, e, f = tests
    global memo_sq_max
    global memo_n_max
    
    if not (a>b and c>d and e>f and a>c and c>e and b<c and b<d and d>f and
            (a-b)%2==0 and (c-d)%2==0 and (e-f)%2==0 and max(a,b,c,d,e,f) == a):
        return False
    
    for n in tests:
        while n > memo_sq_max:
            memo_n_max += 1
            memo_sq_max = memo_n_max ** 2
            memo.add(memo_sq_max)
        if n not in memo:
            return False
        # if n != int(sqrt(n)) ** 2:
            # return False
    return True

def xlower(total):
    total += 3
    return total // 3 + (1 if total % 3 != 0 else 0)
def ylower(totalsub):
    totalsub += 1
    return totalsub // 2 + (1 if totalsub % 2 != 0 else 0)
def inc_n(n):
    while True:
        yield n
        n += 1
def main():
    for total in inc_n(6):
        x_upper = total - 3
        x_lower = xlower(total)
        for x in range(x_lower, x_upper+1):
            y_upper = (total - x) - 1
            y_lower = ylower(total - x)
            for y in range(y_lower, y_upper+1):
                z = total - x - y
                if is_psq(x, y, z):
                    return x+y+z
                # else:
                    # print(x, y, z, total)
        
print(main())
