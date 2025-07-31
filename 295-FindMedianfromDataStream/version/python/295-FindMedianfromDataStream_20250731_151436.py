# Last updated: 7/31/2025, 3:14:36 PM
# Use dfs to solve and pick the correct pair
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach - Sort the candidates list, then decide on which element to use and skip
        # - 
        # TC - O(n * 2^n)
        # SC - O(n)

        result = []
        candidates.sort()


        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if total > target or i  == len(candidates):
                return
            
            # include element candidates[i]
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()

            # skipping element candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs (i+1, curr, total)
        
        dfs(0, [], 0)
        return result