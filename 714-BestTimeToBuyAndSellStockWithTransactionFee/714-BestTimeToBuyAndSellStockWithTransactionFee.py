# Last updated: 7/26/2025, 2:32:23 PM
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Approach - check at each instance for the max profit and return the final value. During calculation of profit subtract fee as well
        # TC - O(n) SC - O(1)

        n = len(prices)
        profit = 0
        effectiveBuy = prices[0]

        for i in range(n):
            profit = max(profit, (prices[i] - effectiveBuy - fee))
            effectiveBuy = min(effectiveBuy, (prices[i] - profit))
        return profit