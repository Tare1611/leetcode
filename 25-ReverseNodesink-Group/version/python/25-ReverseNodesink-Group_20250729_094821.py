# Last updated: 7/29/2025, 9:48:21 AM
# Use DFS based recursion to invert
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Approach - Use DFS to recusively go through the children and swap them. 
        # TC - O(n)
        # SC - O(n) Due to recursion stack

        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root