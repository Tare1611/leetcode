# Last updated: 7/24/2025, 2:37:00 PM
# Approach Binary Search to reduce TC and SC
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Approach - Use binary search to have TC - O(logn) return l which is the highest element
        # TC - O(logn) SC - O(1)
        
        n = len(nums)
        l = 0
        r = n-1
        mid = 0

        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l  = mid + 1
        return l