# Last updated: 7/25/2025, 1:59:31 PM
# Recursive approach with DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach - Have two variables to store the rob amount, 1 starts at first, 2 starts at second house. Calculate recursively further ahead.
        # TC - O(n) SC - O(1) 
        rob1, rob2 = 0, 0
        n = len(nums)
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2