# Last updated: 7/18/2025, 12:34:12 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #  Approach 2 pointers requires sorting, and a removal flag
        # TC - O(nlogn) SC - O(1)
        nums.sort()
        l = 0
        r = len(nums) - 1
        check = 0
        while l < r:
            if nums[l] + nums[r] == k:
                check += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else: 
                r -= 1
        return check
        
