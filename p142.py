

# Problem 142: Perfect Square Collection
# https://projecteuler.net/problem=142

memo_i_max = 500
memo = [i**2 for i in range(memo_i_max+1)] # note: contains 0**2
def sq(i):
    global memo_i_max
    if i > memo_i_max:
        for j in range(memo_i_max+1, i+100+1):
            memo.append(j**2)
        memo_i_max = i+100
    # for tmp in range(memo_i_max+1, i+1):
        # memo.append(tmp**2)
    # memo_i_max = i
    return memo[i]
        
def inc_n(n):
    while True:
        yield n
        n += 1

def main():
    for ai in inc_n(4):
        for bi in range(1, ai):
            a2, b2 = sq(ai), sq(bi)
            if (a2-b2)%2==0:
                x, y = (a2+b2)//2, (a2-b2)//2
                di, ci = bi+1, ai-1
                d2, c2 = sq(di), sq(ci)
                while d2 < x < c2:
                    if x-d2 > c2-x:
                        di += 1
                        d2 = sq(di)
                    elif x-d2 < c2-x:
                        ci -= 1
                        c2 = sq(ci)
                    elif x-d2 == c2-x:
                        z = (c2-d2)//2
                        if y+z in memo and y-z in memo:
                            print(x, y, z)
                            return x+y+z
                        else:
                            di += 1
                            d2 = sq(di)
                    else: 
                        print("Boing!")
                        
print(main())   # 1006193  x y z (434657, 420968, 150568)


