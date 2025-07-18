# Last updated: 7/17/2025, 9:32:21 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        for r in range(n):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        