# Last updated: 8/5/2025, 1:02:11 PM
# Use a q to store the value of node in a level
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach - Traverse through the tree in BFS way. 
        # - Store the the values of each level in a list and then append the list to final result.
        # - 
        # TC - O()
        # SC - O()

        result = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result