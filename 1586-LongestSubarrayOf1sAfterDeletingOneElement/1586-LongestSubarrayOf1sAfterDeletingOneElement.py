# Last updated: 7/19/2025, 12:45:10 AM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Bruteforce Approach - use nested for loop
        # TC - O(n^2) SC - O(1)
        # n = len(nums)
        # max_len = 0
        # for i in range(n):
        #     zero_count = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             zero_count += 1
        #         if zero_count > 1:
        #             break
        #         max_len = max(max_len, j - i + 1)
        # return max_len - 1

        # Optimal Approach - Use Sliding Window approach to check for the values
        # TC - O(n) SC - O(1)
        n = len(nums)
        left = max_len = zero_count = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len - 1