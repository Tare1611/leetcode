# Last updated: 7/20/2025, 4:26:53 PM
# Use dfs in recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Approach: Use dfs and prefix sum to count
        # TC - O(n) SC - O(h + n)
        from collections import defaultdict
        prefix = {0:1}
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix.get(curr_sum - targetSum, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1
            return count

        prefix = defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0)