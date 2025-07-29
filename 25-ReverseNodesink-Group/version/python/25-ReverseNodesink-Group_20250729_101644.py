# Last updated: 7/29/2025, 10:16:44 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def recursion(root):
            nonlocal diameter
            if root is None:
                return 0
            left = recursion(root.left)
            right = recursion(root.right)
            diameter = max(diameter,left + right)
            return max(left,right)+1
        
        recursion(root)
        return diameter