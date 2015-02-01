

# Problem 32: Pandigital products
# https://projecteuler.net/problem=32

from itertools import permutations as perm

ds = '123456789'

def is_pandigital(num):
    ins = sum(1 for d in ds if d in num)
    return ins == len(ds)
            
def main():
    result = set()
    answers = set()
    for i in ds: # 1 4 4
        for jli in perm(ds[0:int(i)] + ds[int(i)+1:], 4):
            j = ''.join(jli)
            k = str(int(i) * int(j))
            if len(k) == 4 and is_pandigital(i + j + k):
                result.add((i, j, k))
                answers.add(int(k))
    for ili in perm(ds, 2): # 2 3 4
        for jli in perm(''.join(set(ds)-set(ili)), 3):
            i = ''.join(ili)
            j = ''.join(jli)
            k = str(int(i) * int(j))
            if len(k) == 4 and is_pandigital(i + j + k):
                result.add((i, j, k))
                answers.add(int(k))
    return sum(answers)

print(main())
