# Last updated: 7/27/2025, 12:43:33 PM
# Updated Binary search to check for the existence of value
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Approach - Use Binary Search and return the target value
        # TC - O(logn) SC - O(1)
        left = 0 
        right = len(nums) - 1        

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1