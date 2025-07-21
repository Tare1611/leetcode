# Last updated: 7/20/2025, 7:53:23 PM
# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Approach - Use BFS for each level and keep a track
        # TC - O(n) SC - O(w) width of tree.
        from collections import deque
        if not root:
            return []
        
        right_view = []
        queue = deque([root])
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()

                if i == level_length - 1:
                    right_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_view