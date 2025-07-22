# Last updated: 7/22/2025, 12:37:55 PM
# Iterative Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursive Approach - Using a function to handle the calculation
        # TC - O(n) SC - O(h) - due to call stack
        # def dfs(node: Optional[TreeNode], val):
        #     if not node:
        #         return None
        #     if node.val == val:
        #         return node
        #     elif node.val < val:
        #         return dfs(node.right, val)
        #     elif node.val > val:
        #         return dfs(node.left, val)
        
        # return dfs(root, val)
        # Iterative Approach - Using while loop to check since we just have to return the node so can avoid recursion.
        # TC - O(n) and SC - O(1)
        if not root:
            return None
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
        