# Last updated: 7/20/2025, 8:15:35 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach - Use dfs recursively and select the max value from the nodes
    # TC - O(n) SC - O(h)
    def goodNodes(self, root: TreeNode) -> int:
        good = 1
        path = []
        def dfs(node, max_val):
            if not node: 
                return 0 
            good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)

            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)

            return good + left + right
        return dfs(root, root.val)
