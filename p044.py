

# Problem 44: Pentagon numbers
# https://projecteuler.net/problem=44

# want to find out (the minimized) Pj and Pk, return Pk - Pj
# P1 P2 P3 ... Pi ... Pj ... Pk ... Pn
# Pk - Pj = Pi  in the set
# Pk + Pj = Pn  in the set
# Pn - Pk  in the set
# add) 2Pk = Pi + Pn,  Pn - 2Pk = Pi in the set
# Pi = Pk - Pj  which is the answer

def main():
    pn_set = set()
    n = 1
    while True:
        pn = n * (3*n-1) // 2
        for pk in pn_set:
            if pn-pk in pn_set and pn-2*pk in pn_set:
                return pn-2*pk
        pn_set.add(pn)
        n += 1

print(main())
