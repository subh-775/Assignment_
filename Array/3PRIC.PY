# MAXIMUM PROFIT
def maxProfit(prices: list[int]) -> int:
    minm = min(prices)
    ind_min = prices.index(minm)
    if ind_min == len(prices)-1:
        temp_lst = [0]
    else:
        temp_lst = prices[ind_min:]

    profit = max(temp_lst) - minm
    if profit < 0:
        return 0
    else:
        return profit

prices = [7,1,5,3,6,4]

print(maxProfit(prices))