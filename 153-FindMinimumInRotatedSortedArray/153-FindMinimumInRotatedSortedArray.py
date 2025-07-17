# Last updated: 7/16/2025, 8:14:58 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute force or intuitive approach - run a for loop. Since the loop runs for the whole list not good TC
        # # TC - O(n) SC - O(1)
        # n = len(nums)
        # if n > 0:
        #     small = nums[0]
        # else:
        #     return 0
        # # small = 
        # for i in range(n):
        #     small = min(small, nums[i])
        # return small

        # Optimal Approach would be to use Binary sort instead and find the minimum.
        # TC - O(logn) SC - O(1)
        n = len(nums)
        left = 0
        right = n-1
        # small = nums[left]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left =  mid + 1
            else: 
                right = mid
        return nums[left]