

def divisors(n):
    result = [1]
    upper = n // 2
    i = 2
    while i < upper:
        if n % i == 0:
            result.append(i)
            upper = n // i
            result.append(upper)
        i += 1
    return result

def sum_divisors(n):
    return sum(divisors(n))

print(divisors(220))
print(sum_divisors(220))
print(divisors(284))
print(sum_divisors(284))

def amicable(a):
    b = da = sum_divisors(a)
    db = sum_divisors(b)
    if a != b and a == db and b == da:
        return b
    else:
        None

print(amicable(220))
print(amicable(284))

set_amicable = set()
for n in range(1, 10000):
    b = amicable(n)
    if b:
        set_amicable.add(n)
        set_amicable.add(b)

print(sum(set_amicable))
