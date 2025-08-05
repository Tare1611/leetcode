# Last updated: 8/5/2025, 5:46:07 PM
# Use backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Approach - Since it is combinations we can select the first element and have combination pairs for the right side.
        # - Store in result array, and use backtrack to go through the whole list of numbers and their combinations 
        # TC - O(C(n, k)*k)
        # SC - O(C(n, k)*k)

        result = []

        def backtrack(start, comb):
            if len(comb) == k:
                result.append(comb.copy())
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        backtrack(1, [])
        return result