# Last updated: 8/1/2025, 5:31:54 PM
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
        # - Use pointer l to identify the start and pointer r to traverse the len(str) result is the difference between
        # - pointer r and l + 1 for 0 index
        # - Have a char Set to store the unique values
        # TC - O(n) SC - O(n)
        
        l = 0
        charSet = set()
        result = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result
