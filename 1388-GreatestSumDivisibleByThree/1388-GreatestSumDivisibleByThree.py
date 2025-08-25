# Last updated: 8/24/2025, 8:13:05 PM
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Approach - Maintain a DP Array to store the values of the max sum that gives remainder 0, 1, 2
        # - For each element copy the dp and perform the calculations
        # - For each remainder update the dp
        # - Return dp[0] for the final answer

        dp = [0, float('-inf'), float('-inf')]

        for num in nums:
            curr = dp[:]

            for r in range(3):
                newRemain = (r + num) % 3
                dp[newRemain] = max(dp[newRemain], curr[r] + num)
        
        return dp[0]


