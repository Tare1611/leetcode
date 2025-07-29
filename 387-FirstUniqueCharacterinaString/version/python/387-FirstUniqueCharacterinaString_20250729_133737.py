# Last updated: 7/29/2025, 1:37:37 PM
# Use a two pointer approach
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l <= r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
