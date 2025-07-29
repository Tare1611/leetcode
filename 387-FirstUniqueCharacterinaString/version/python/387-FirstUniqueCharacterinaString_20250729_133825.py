# Last updated: 7/29/2025, 1:38:25 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Approach - Two pointer, replace the element
        # TC - O(n)
        # SC - O(1)
        l = 0
        r = len(s) - 1

        while l <= r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
