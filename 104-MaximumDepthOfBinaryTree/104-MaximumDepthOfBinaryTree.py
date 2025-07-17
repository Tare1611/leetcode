# Last updated: 7/16/2025, 8:15:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Brute force approach - Level order traversal using queue
        # TC - O(n), SC - O(n)
        # if not root:
        #     return 0
        # from collections import deque
        # q = deque([root])
        # depth = 0
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left: q.append(node.left)
        #         if node.right: q.append(node.right)
        #     depth += 1
        # return depth
        # Optimal Approach - Recursion to calculate depth
        # TC - O(n), SC - O(h)
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))