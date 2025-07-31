# Last updated: 7/31/2025, 6:38:48 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Approach - Use DFS to recursively go through the List and generate the subsets.
        # TC - O(n * 2^n)
        # SC - O(2^n)

        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            # include the element
            subset.append(nums[i])
            dfs(i + 1)
            # not include the element
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result