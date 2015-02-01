

# Problem 156: Counting Digits
# https://projecteuler.net/problem=156

#
def k(w):
    return w * (10 ** (w-1))
def f(n, d):
    ns = str(n)
    if len(ns) == 1:
        return 1 if n >= d else 0
    else:
        ns_head = ns[0]
        n_head = int(ns_head)
        ns_remaining = ns[1:]
        n_remaining = int(ns_remaining)
        w = len(ns_remaining)
        tmp = n_head * k(w)
        if n_head > d:
            tmp += 10**w
        elif n_head == d:
            tmp += n_remaining + 1
        # ((10**w) if n_head >= d else 0)
        return tmp + f(n_remaining, d)
def sum_f(n_lower, n_upper, d):
    fn_lower = f(n_lower, d)
    fn_upper = f(n_upper, d)
    # print(n_lower, n_upper, fn_lower, fn_upper)
    if n_lower > n_upper:
        return []
    elif n_lower == fn_lower:
        # print(n_lower)
        return [n_lower] + sum_f(n_lower+1, n_upper, d)
    elif n_upper == fn_upper:
        # print(n_upper)
        return [n_upper] + sum_f(n_lower, n_upper-1, d)
    elif n_lower < fn_lower:
        return sum_f(fn_lower, n_upper, d)
    elif n_upper > fn_upper:
        return sum_f(n_lower, fn_upper, d)
    elif n_lower > fn_lower or n_upper < fn_upper:
        n_middle = (n_lower+n_upper)//2
        return sum_f(n_lower, n_middle, d) + sum_f(n_middle+1, n_upper, d)
    else:
        print('error')
def sum_f2(n_lower, n_upper, d):
    result = sum_f(n_lower, n_upper, d)
    # print(sorted(result))
    print(max(result))
    return sum(result)
# print(sum_f(0, 199981, 1))   # 199981
# print('-' * 20)
# print(sum_f2(0, 1111111110, 1))  # 22786974071
# print('-' * 20)
# print(sum_f(0, 22786974071, 1))  # 22786974071
# print('-' * 20)

# for d in range(1, 9+1):
    # print(sum_f2(0, 99999999999, d))
    # print('-' * 30)

# f(n, 1) max 1111111110      s(1) 22786974071
# f(n, 2) max 10535000000     s(2) 73737982962
# f(n, 3) max 20500000000     s(3) 372647999625
# f(n, 4) max 30500000000     s(4) 741999999540
# f(n, 5) max 40000000000     s(5) 100000000000
# f(n, 6) max 59628399995     s(6) 2434703999430
# f(n, 7) max 69971736170     s(7) 1876917059570
# f(n, 8) max 79998399997     s(8) 15312327487352
# f(n, 9) max 80000000000     s(9) 360000000000
#                                  21295121502550 answer

# print(sum_f(0, 99999999999, 1))
# print('-' * 20)

# 99999999999?  why? 
def main():   
    return sum(sum_f2(0, 99999999999, d) for d in range(1, 9+1))
print(main())

# see problem
# why s(d) exists? If exists, that means once beyond nmax, f(nmax, d) always > nmax
# how to prove it?  
# 1: n increases too fast, f(n, d) can't catch up
# 2: or  f(n, d) increases too fast, n can't catch up   <- I think this is it.
# how to calculate the lower bound of nmax?
# 1111111110  10-digit 


# print(f(1111111109, 1))  # 1111111101
# print(f(1111111110, 1))  # 1111111110
# print(f(1, 1))
# print(f(9, 1))
# print(foo(199981, 1))
# print(f(199980, 1))
# print(f(199981, 1))
# print(f(199982, 1))
# print(f(199999, 1))

def foo(n, d):  # to check f
    result = 0
    for i in range(n+1):
        for c in str(i):
            if int(c) == d:
                result += 1
    return result

