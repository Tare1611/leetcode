# Last updated: 7/31/2025, 6:38:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Approach - Use dfs to check if all the nodes follow the condition or not.
        # - Condition is left is smaller than root
        # - Right is larger than the Root.
        # - Check for this condition recursively.
        # TC - O(n)
        # SC - O(n) - For recursion stack, else for each iteration it would be O(1)

        def dfs(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))
        return dfs(root, float("-inf"), float("inf"))