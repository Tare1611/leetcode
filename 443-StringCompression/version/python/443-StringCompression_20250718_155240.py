# Last updated: 7/18/2025, 3:52:40 PM
# Optimal approach is to use sliding approach
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Brute Force Approach - 2 For loop 
        # TC - O(n^2) SC - O(1)
        # n = len(nums)
        # max_len = 0

        # for i in range(n):
        #     zero_count = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             zero_count += 1
        #         if zero_count > k:
        #             break
        #         max_len = max(max_len, j-i+1)
        
        # return max_len

        # Optimal Approach - Use sliding window
        # TC - O(n) SC - O(1)
        n = len(nums)
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len