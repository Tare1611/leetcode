# Last updated: 7/25/2025, 3:02:33 PM
# 2-D DP array to store values, start from the bottom instance
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Approach - MAintain a 2-D array and store the values of common in substring while checking if first ch is same.
        # Bottom Up approach
        # TC - O(n*m) SC - O(n*m)

        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0] 