# Last updated: 7/31/2025, 7:20:23 PM
# Backtracking since we have to brute force all the solution values
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Approach - We will have to brute force all the possible outcomes, so we use the Backtracking to perform the task.
        # TC - O(n * 2^n)
        # SC - O(n * 2^n)
        result = []
        nums.sort()

        def backTrack(i, subset):
            # base case 
            if i==len(nums):
                result.append(subset[::])
                return

            # recursive case
            # Subset that include nums[i]

            subset.append(nums[i])
            backTrack(i+1, subset)
            subset.pop()

            # Subset that do not include nums[i]

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backTrack(i+1, subset)
        backTrack(0, [])
        return result