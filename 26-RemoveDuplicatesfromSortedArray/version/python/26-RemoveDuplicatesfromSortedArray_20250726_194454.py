# Last updated: 7/26/2025, 7:44:54 PM
# Two Pointer setup
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Approach - Use two pointer setup. Start from index 1 and then move ahead when you find a new value.
        # TC - O(n) SC - O(1)
        left = 1
        
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

        return left