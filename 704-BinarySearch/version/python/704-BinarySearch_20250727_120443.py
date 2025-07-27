# Last updated: 7/27/2025, 12:04:43 PM
# Simple Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Approach - Implement Binary Search
        # TC - O(logn) SC - O(1)
        left = 0
        right = len(nums) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1