# Last updated: 7/22/2025, 1:28:30 PM
# Iterative Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Recursive Approach with helper function
        # TC- O(h) where h can be logn - n SC - O(h) recursion stack height
    #     if not root:
    #         return None

    #     if key < root.val:
    #         root.left = self.deleteNode(root.left, key)
    #     elif key > root.val:
    #         root.right = self.deleteNode(root.right, key)
    #     else:
    #         # Node found - 3 cases - only node, one child and two child 
    #         if not root.left and not root.right:
    #             return None
            
    #         if not root.left:
    #             return root.right
    #         elif not root.right:
    #             return root.left
            
    #         min_node = self.getMin(root.right)
    #         root.val = min_node.val
    #         root.right = self.deleteNode(root.right, min_node.val)
        
    #     return root

    # def getMin(self, node: TreeNode) -> TreeNode:
    #     while node.left:
    #         node = node.left
    #     return node

        # Iterative Approach: Use a loop to reach the node, and then use a helper function
        # TC - O(h) height of tree SC - O(1)
        if not root:
            return None
        
        parent = None
        curr = root

        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            
        if not curr:
            return root

        def del_node(node: TreeNode) -> TreeNode:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            succ_parent = node
            succ = node.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            
            if succ_parent != node:
                succ_parent.left = succ.right
                succ.right = node.right
            succ.left = node.left
            return succ

        if not parent:
            return del_node(curr)
        
        if parent.left == curr:
            parent.left = del_node(curr)
        else:
            parent.right = del_node(curr)
        
        return root
