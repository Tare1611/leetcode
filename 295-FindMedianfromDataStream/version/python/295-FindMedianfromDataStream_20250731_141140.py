# Last updated: 7/31/2025, 2:11:40 PM
# Use DFS
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach - Since we use a decision tree to find all possible combinations.
        # - We will use dfs recursively to generate the all combinations that add up to the target
        # TC - O(2^t) where t is target
        # SC - O(t)

        result = []
        
        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
        dfs(0, [], 0)
        return result     