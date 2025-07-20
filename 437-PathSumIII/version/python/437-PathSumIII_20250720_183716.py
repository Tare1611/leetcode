# Last updated: 7/20/2025, 6:37:16 PM
# Approach - Recursively traverse the tree to find p and q
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Approach traverse the tree recursively to check for p and q and return root.
        # TC - O(n) SC - O(n)[recursion]
        if not root:
            return None
        
        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r