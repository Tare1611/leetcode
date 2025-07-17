# Last updated: 7/16/2025, 8:14:39 PM
class Solution:
    def maxPower(self, s: str) -> int:
        # Brute force - Use two for loop to go through the string
        # TC - O(n^2) SC - O(1)
        # count = 1
        # max_count = 1
        # n = len(s)
        # for i in range(n):
        #     count = 1 
        #     for j in range(i + 1, n):
        #         if s[i] == s[j]:
        #             count += 1
        #         else:
        #             break
        #     max_count = max(max_count, count)
        # return max_count       
        
        # Optimal Approach - Use a single loop and check the feedback value from previous i value
        # TC - O(n) SC - O(1)
        
        count = 1
        max_count = 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count
