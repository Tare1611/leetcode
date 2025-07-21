# Last updated: 7/21/2025, 4:38:07 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # profit = 0

        # # iterating over the prices array list
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        # return max_profit

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        return max_profit            