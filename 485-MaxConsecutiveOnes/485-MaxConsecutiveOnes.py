# Last updated: 8/26/2025, 10:48:49 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Approach - Use a single loop
        # - Check if current element is 1, increment the counter
        # - Have a max counter and update the count of consecutive ones
        # TC - O(n)
        # SC - O(1)

        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else: 
                count = 0
            max_count = max(max_count, count)
        return max_count