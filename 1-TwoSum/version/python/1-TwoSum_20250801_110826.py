# Last updated: 8/1/2025, 11:08:26 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach - To optimize time complexity we can create a dictionary with the pairs of the value and the remainder from the subtraction from target. 
        # Run a loop to find the valid pair.
        # TC - O(n)
        # SC - O(n)

        n = len(nums)
        numDict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in numDict:
                return[numDict[complement], i]
            numDict[num] = i
        return []