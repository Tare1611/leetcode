# Last updated: 7/29/2025, 10:16:25 AM
# Use DFS to traverse through the right left subtree and return the max length
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Approach - Use recursive DFS to check for the length of the left and right side of tree and add one to res
        # TC - O(n)
        # SC - O(n) Due to recursion stack used by system to track

        self.result = 0
        
        def dfs(curr):
            # returns height not diameter
            if not curr: 
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.result = max(self.result, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        
        return self.result