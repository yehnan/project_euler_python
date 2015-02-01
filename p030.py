

# Problem 30: Digit fifth powers
# https://projecteuler.net/problem=30

# brute force

def limit(power):
    w = 2
    while True:
        num_lower = 10 ** (w - 1)
        sop_upper = (9**power) * w
        if num_lower > sop_upper:
            return w-1
        w += 1

print(limit(4))   # 5
print(limit(5))

def is_sop(n, power):
    sop = sum(int(c)**power for c in str(n))
    return n == sop

def main(power):
    result = 0
    for n in range(10, 10**limit(power)):
        if is_sop(n, power):
            result += n
    return result

print(main(4))
print(main(5))
