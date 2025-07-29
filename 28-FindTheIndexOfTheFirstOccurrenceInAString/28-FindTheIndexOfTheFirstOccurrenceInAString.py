# Last updated: 7/29/2025, 11:02:42 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Approach - go through the haystack and track the needle with if statement.
        # TC - O(m*n) SC -O(n)
        
        n = len(needle)
        for i in range(len(haystack)):
            # print(haystack[i: i+(n)])
            if needle in haystack[i:i+n]:
                return i
            
        return -1