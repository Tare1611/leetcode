# Last updated: 7/16/2025, 8:15:19 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force approach - Use set to store unique values, nested for loop to travel through. 
        # TC - O(n^2), SC - O(n)
        # n = len(s)
        # res = 0
        # for i in range(n):
        #     charS = set()
        #     for j in range(i, n):
        #         if s[j] in charS:
        #             break
        #         charS.add(s[j])
        #     res = max(res, len(charS))
        # return res
        # Optimal Approach - Use sliding window and a single loop to traverse through the string and return result
        # TC - O() SC - O()
        l = 0
        charS = set()
        res = 0
        n = len(s)
        for r in range(n):
            while s[r] in charS:
                charS.remove(s[l])
                l += 1
            charS.add(s[r])
            res = max(res, r - l + 1)
        return res
