# Last updated: 7/24/2025, 3:48:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #  Approach - Traverse tree level by level using bfs. Use deque for help.
        # TC - O(n) SC - O(w) width of tree
        from collections import deque
        if not root:
            return 0
        
        level = 1
        max_level = 1
        max_sum = float('-inf')

        q = deque([root])

        while q:
            level_size = len(q)
            current_sum = 0

            for _ in range(level_size):
                node = q.popleft()
                current_sum += node.val
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = level
            
            level += 1
        return max_level
