# Last updated: 7/18/2025, 12:34:26 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Basic two pointer approach, one traverses the s str, and other traverses the t str.
        # TC - O(n) where n is len of t, SC - O(1)
        n = len(s)
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == n
