# Last updated: 7/16/2025, 8:15:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Using recursion to check through all the values in the tree up to the root.
        # different function to perform recursion as we need extra values to be returned.
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

        