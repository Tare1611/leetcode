# Last updated: 7/16/2025, 8:14:51 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        return nums[n-k]