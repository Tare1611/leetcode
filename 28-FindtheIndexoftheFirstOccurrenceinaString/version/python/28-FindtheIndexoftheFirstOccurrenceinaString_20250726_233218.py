# Last updated: 7/26/2025, 11:32:18 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Approach - 
        # TC - O(n) SC -O()
        
        n = len(needle)
        for i in range(len(haystack)):
            print(haystack[i: i+(n)])
            if needle in haystack[i:i+n]:
                return i
            
        return -1