# Last updated: 7/26/2025, 2:32:34 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Approach - Setup a DP to track the 1's
        # TC - O(n) SC - O(n)

        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp