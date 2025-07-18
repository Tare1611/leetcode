# Last updated: 7/18/2025, 2:02:42 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Brute Force Approach - 2 for loop
        # TC - O(n^2) SC - O(1)
        # avg = 0
        # max_avg = float(-inf)
        # sum1 = 0
        # n = len(nums)
        # for i in range(n - k + 1):
        #     sum1 = 0
        #     for j in range(i, i+k):
        #         sum1 = sum1 + nums[j]
        #     avg = float(sum1/k)
        #     max_avg = max(max_avg, avg)
        
        # return max_avg

        # Optimal Approach - Sliding Window approach to move ahead
        # TC - O(n) SC - O(1)
        
        window = sum(nums[:k])
        max_sum = window

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            max_sum = max(max_sum, window)
        return max_sum/k