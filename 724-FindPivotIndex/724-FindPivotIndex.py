# Last updated: 7/19/2025, 12:45:18 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Brute Force Approach - Using two different arrays to store values and then comparing.
        # TC - O(n) SC - O(n)
        # n = len(nums)
        # leftsum = [0] * (n + 1)
        # rightsum = [0] * (n + 1) 

        # for i in range(n):
        #     leftsum[i+1] = leftsum[i] + nums[i]
        
        # for i in range(n -1, -1, -1):
        #     rightsum[i] = rightsum[i + 1] + nums[i]

        # for i in range(n):
        #     if leftsum[i] == rightsum[i + 1]:
        #         return i
        # return -1   

        # Optimal Approach - To minimise the use of Space and have SC - O(1)
        # TC - O(n) SC - O(1)
        leftsum = 0
        total = sum(nums)

        for i, num in enumerate(nums):
            if leftsum == total - leftsum - num:
                return i
            leftsum += num
        return -1
