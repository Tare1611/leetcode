# Last updated: 7/16/2025, 8:15:20 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force use 2 for loops to go over the array and check for the target
        # TC - O(n^2) SC - O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j
        # Optimal Approach - Use a dictionary single loop and check for the remainder
        # 
        num_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index:
                return [num_index[complement], i]
            num_index[num] = i
        return []            