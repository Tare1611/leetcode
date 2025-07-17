# Last updated: 7/17/2025, 12:45:08 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Optimal Approach - find the max and work on the bool list
        # TC - O(n) SC - O(n) 
        maxCandies = []
        high = max(candies)
        print(high)

        for candy in candies:
            check = candy + extraCandies >= high
            maxCandies.append(check)
        # print(maxCandies)
        return maxCandies