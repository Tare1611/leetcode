# Last updated: 7/20/2025, 8:15:37 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Approach - Use dfs with direction and length to track
        # TC - O() SC - O()
        self.maxlen = 0
        def dfs(node, direction, length):
            if not node:
                return 
            
            self.maxlen = max(self.maxlen, length)
            
            if direction == "left":
                dfs(node.left, "right", length + 1)
                dfs(node.right, "left", 1)
            else:
                dfs(node.right, "left", length + 1)
                dfs(node.left, "right", 1)
        
        dfs(root.left, "right", 1)
        dfs(root.right, "left", 1)

        return self.maxlen
