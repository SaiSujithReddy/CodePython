class Denominations:
    def __init__(self,coins,total_sum):
        self.coins = coins
        self.total_sum = total_sum
        self.result = total_sum
        #self.temp_result = 0
        #sorted_coins = sorted(self.coins)

    def find_min_denominations(coins1,total_sum):
        result = total_sum
        if total_sum in coins1:
            return 1
        else:
            for i in [x for x in coins1 if x<= total_sum]:
                temp_result = 1 + find_min_denominations(coins1,total_sum-i)
                if temp_result < result:
                    result = temp_result
        return result


coins = [1,2,5,10]
total_sum = 12
den = Denominations(coins,total_sum)
print(den.find_min_denominations(coins,total_sum))