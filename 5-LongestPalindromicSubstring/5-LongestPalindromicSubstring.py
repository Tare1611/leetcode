# Last updated: 8/4/2025, 5:14:41 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach - Start from the mid and keep checking the left and right values if they are equal or not. 
        # TC - O(n^2)
        # SC = O(n)

        result = ""
        resultLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r+1]
                    resultLen = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r + 1]
                    resultLen = r - l + 1
                l -= 1
                r += 1
        return result