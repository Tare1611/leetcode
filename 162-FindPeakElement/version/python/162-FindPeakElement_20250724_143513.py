# Last updated: 7/24/2025, 2:35:13 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if not nums:
        #     return []
        
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