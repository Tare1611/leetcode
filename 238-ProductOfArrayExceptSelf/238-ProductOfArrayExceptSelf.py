# Last updated: 7/16/2025, 8:14:49 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force Approach - Use two for loops to go via array and multiply elements
        # TC - O(n^2)
        # n = len(nums)
        # result = [1]*n
        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if i!=j:
        #             product*=nums[j]
        #     result[i] = product
        # return result
        # Optimal Approach - USe prefix sum to speed up process
        # TC - O(n)
        n = len(nums)
        result = [1]*n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range (n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result