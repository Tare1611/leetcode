# Last updated: 7/23/2025, 3:04:50 PM
# Brute Force Approach just sort and do length - k
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Brute Force or intuitive approach is to sort the array and then return required value.
        # TC - O(nlogn) - sort function TC, SC - O(1)
        nums.sort()
        n = len(nums)
        return nums[n-k]
