

# Problem 29: Distinct powers
# https://projecteuler.net/problem=29

def main(al, ah, bl, bh):
    ps = set()
    for a in range(al, ah+1):
        for b in range(bl, bh+1):
            ps.add(a**b)
    return len(ps)

# print(main(2, 5, 2, 5))  # 15
print(main(2, 100, 2, 100))

