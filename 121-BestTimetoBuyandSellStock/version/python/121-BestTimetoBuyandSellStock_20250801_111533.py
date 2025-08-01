# Last updated: 8/1/2025, 11:15:33 AM
# Used a single loop to travers and keep a track of min price and max profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #  Approach - Go through the whole array and keep a check on the prices and profit.
    # Two ways - nested for loop - very time consuming
    # - Single loop with keeping track of minimum price and max price in order.

        minPrice = float("inf")
        maxPrice = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                maxPrice = max(maxPrice, profit)
        return maxPrice