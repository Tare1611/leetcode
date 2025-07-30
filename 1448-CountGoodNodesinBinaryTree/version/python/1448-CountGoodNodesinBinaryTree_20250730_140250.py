# Last updated: 7/30/2025, 2:02:50 PM
# Use inorder traversal and append all the values in an array, return the kth element.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach - Perform inorder traversal and store the values in array and return the kth element.
        # - Use DFS to perform the traversal
        # TC - O(n)
        # SC - O(n)
        arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)

        return arr[k-1]