# Last updated: 7/16/2025, 8:15:02 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force Approach - Nested for loops
        # TC - O(n^2), SC - O(1)
        # n = len(prices)
        # max_profit = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if prices[j] - prices[i] > 0:
        #             profit = prices[j] - prices[i]
        #             max_profit = max(max_profit, profit)
        # return max_profit
        # Optimal Approach - Single Pass
        # TC - O(n), SC - O(1)
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # update the minimum price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)  # update max profit if better
        return max_profit