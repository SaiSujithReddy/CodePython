# this is partial working solution
# doesn't work for -1 test case (where amount cannot be find by sum or multiple of coins)

'''
MEDIUM:  You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
Example 1:coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)
Example 2:coins = [2], amount = 3
return -1.
Note:You may assume that you have an infinite number of each kind of coin.
'''

import sys

def dpFindChange(coins_list,total_sum,result):
    for denomination in range(total_sum+1):
        coin_count = denomination
        print("value of coin_count is {}, value of denomination is {}".format(coin_count,denomination))
        for j in [c for c in coins_list if c <= denomination]:
            print("value of j is {}".format(j))
            print("result[denomination-j] +1 {}".format(result[denomination-j] +1))
            print("coin_count {}".format(coin_count))
            if result[denomination-j] +1 < coin_count:
                coin_count = result[denomination-j]+1
        result[denomination] = coin_count
        print("value of result is {}".format(result))
    return result[total_sum]

coins = [2,5,10]
total_sum = 13
result = [sys.maxint]*(total_sum+1)
result[0] = 0

print(dpFindChange(coins,total_sum,result))

if result[total_sum] == sys.maxint:
    print(-1)
else :
    print("Number of coins needed for getting total_sum ({} in this case) is {}".format(total_sum,result[total_sum]))
# 12 is two times 5 plus 2 or 1 time ten plus 2
