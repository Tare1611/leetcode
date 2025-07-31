# Last updated: 7/31/2025, 6:38:43 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Approach - Prorder always has the root first and then it's left and right child nodes. 
        # - Inorder helps find the partition between left subtree and right subtree.
        # TC - O(n^2)
        # SC - O(n)

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid+1:])
        
        return root