# Last updated: 7/17/2025, 10:00:45 AM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # First Approach - Using while loop and string manipulation.
        # TC - O(m + n) OC - (m + n)
        m = len(word1)
        n = len(word2)
        final = ""
        left, right = 0, 0
        while left < m or right < n:
            if left < m:
                final = final + word1[left]
                left += 1
            
            if right < n:
                final = final + word2[right]
                right += 1
        print(final)
        return final

        # Suggested optimal approach would be to convert the word to list and work on that and then revert to string.
        # TC same as above but 