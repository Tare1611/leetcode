# Last updated: 7/16/2025, 8:15:01 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute Force Approach - clean the string and then compare
        # TC - O(n)
        # SC - O(n)
        # clean_s = ''.join(c.lower() for c in s if c.isalnum())
        # return clean_s == clean_s[::-1]
        # Trying to use less space by utilizing 2 pointer approach
        left, right = 0, len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left += 1
            while left<right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True