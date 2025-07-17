# Last updated: 7/16/2025, 8:14:43 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force Approach - 2 For Loop
        # TC - O(n^2), SC - O(m)
        # n = len(s)
        # res = 0
        # for i in range(n):
        #     count, maxf = {}, 0
        #     for j in range(i, n):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         maxf = max(maxf, count[s[j]])
        #         if ( j - i + 1) - maxf <= k:
        #             res = max(res, j - i + 1)
        # return res
        # Optimal Approach - Sliding Window
        # TC - O(n), SC - O(m)
        n = len(s)
        maxf = 0
        count = {}
        l = 0
        for r in range(n):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(maxf, r - l + 1)
        return res