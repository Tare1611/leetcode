# Last updated: 2/10/2026, 7:53:43 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root1 and not root2:
10            return None
11        
12        v1 = root1.val if root1 else 0
13        v2 = root2.val if root2 else 0
14
15        root = TreeNode(v1 + v2)
16        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
17        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
18
19        return root