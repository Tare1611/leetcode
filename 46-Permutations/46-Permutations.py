# Last updated: 8/4/2025, 5:14:30 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Approach - Use recursion to select the permutation and generate list pf values 
        # TC - O(n! * 2^n)
        # SC - O(n! * n)
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        result = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                result.append(p_copy)
        return result