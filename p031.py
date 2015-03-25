

# Problem 31: Coin sums
# https://projecteuler.net/problem=31

# dynamic programming
def coin_sum(total, coins):
    ways = [1] + ([0] * total)
    for coin in coins:
        for i in range(coin, total+1):
            ways[i] += ways[i - coin]
    return ways[total]

# recursion
def coin_sum_r(total, coins):
    if len(coins) == 1:
        return 1
    elif total < coins[-1]:
        return coin_sum_r(total, coins[:-1])
    else:
        return coin_sum_r(total-coins[-1], coins) + coin_sum_r(total, coins[:-1])

#
coins_england = (1, 2, 5, 10, 20, 50, 100, 200)

#
def test():
    coins_testa = (1, 5, 10, 25) 
    coins_testb = (1, 5, 10, 25, 50, 100)  
    if (coin_sum(100, coins_testa) == 242 and
        coin_sum(100000, coins_testb) == 13398445413854501 and
        coin_sum(200, coins_england) == coin_sum_r(200, coins_england)):
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return coin_sum(200, coins_england)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

