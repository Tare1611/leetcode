# Last updated: 7/20/2025, 8:15:41 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Approach Use - DFS as recursion function to check for the leaf values and append to the array.
        # TC - O( n + m ) SC - O(h1 + h2)

        def dfs(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            dfs(root.left, leaf)
            dfs(root.right, leaf)
        
        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2