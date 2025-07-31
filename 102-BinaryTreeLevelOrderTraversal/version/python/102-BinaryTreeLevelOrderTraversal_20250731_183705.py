# Last updated: 7/31/2025, 6:37:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach - Use BFS and deque to store the node values in every level. Keep a tracking list to store the level nodes and then append it to the result list.
        # TC - O(n)
        # SC - O(n)

        q = collections.deque()
        result = []
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result