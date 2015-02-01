

# Problem 145: How many reversible numbers are there below one-billion?
# https://projecteuler.net/problem=145

# brute force, very slow, rpi runs more than 20 hours

def is_reversible(n):
    ns = str(n)
    ms = ns[::-1]
    m = int(ms)
    
    if len(str(m)) < len(ns):
        return False
    
    tmp = n + m
    for d in str(tmp):
        if d not in '13579':
            return False
    return True

# print(is_reversible(36))   # True
# print(is_reversible(63))   # True
# print(is_reversible(409))  # True
# print(is_reversible(904))  # True

def main(n):
    result = 0
    for i in xrange(10, n+1):
        if i % 10000 == 0:
            print(i)
        if is_reversible(i):
            result += 1
    # sum(1 for i in range(10, n+1) if is_reversible(i))
    return result
print(main(1000))   # 120
print(main(10 ** 9))  # 608720

