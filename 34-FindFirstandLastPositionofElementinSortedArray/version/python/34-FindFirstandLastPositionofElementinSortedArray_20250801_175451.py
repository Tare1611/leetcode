# Last updated: 8/1/2025, 5:54:51 PM
# Binary search move inside from both sides
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Approach - Use binary search with left and right pointers moving towards the target
        # - Return the first instance left meets target, and right meets target
        # - If not present return [-1, -1]

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if (nums[left] == target) and (nums[right] == target):
                return [left, right]
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
        return [-1,-1]