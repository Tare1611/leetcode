# Last updated: 8/2/2025, 2:18:42 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Approach - Use Sliding Window to solve this to keep a track of the len of the substring
        #  - keep a track on length and the count of replacements
        # TC - O(n)
        # SC - O(m)

        count = {}
        result = 0
        l = 0
        maxF = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        return result