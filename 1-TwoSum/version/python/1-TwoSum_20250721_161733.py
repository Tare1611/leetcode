# Last updated: 7/21/2025, 4:17:33 PM
# Optimal Solution with TC O(n) SC O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # complement = Target - i
        # return indices of the i and complement. 
        # Start storing the i value and it's complement in a dictionary so if i find it in the dictionary we can close the loop early.
        num_dict = {}
        # complement = 0

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []