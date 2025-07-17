# Last updated: 7/16/2025, 8:14:50 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute Force Approach - Two for loop, with if block
        # TC - O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        # Optimal Approach - Use hash set to store the seen values
        # TC - O(n)
        # Hash Set 
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        