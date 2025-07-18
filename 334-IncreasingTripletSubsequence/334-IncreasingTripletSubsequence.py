# Last updated: 7/17/2025, 8:39:28 PM
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Brute Force Approach - use nested for loop to check
        # TC - O(n^3) SC - O(1)
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[j] > nums[i]:
        #             for k in range(j+1, n):
        #                 if nums[k] > nums[j]:
        #                     return True
        # return False

        # Optimal Approach - Greedy Way - 
        # TC - O(n) SC - O(n)
        first = float(inf)
        second = float(inf)

        for num in nums:
            if num <= first:
                first = num
            elif  num <= second:
                second = num
            else:
                return True
        return False
