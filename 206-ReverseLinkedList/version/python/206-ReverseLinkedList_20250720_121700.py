# Last updated: 7/20/2025, 12:17:00 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force Approach -  Use stack to reverse the linked list 
        # TC - O(n), SC - O(n)
        # stack = []
        # curr = head 

        # if not head or not head.next:
        #     return head
        
        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        
        # curr = head

        # while stack:
        #     curr.val = stack.pop()
        #     curr = curr.next
        # return head

        # Optimal Approach - Reverse the linked list iteratively. Return prev
        # TC - O(n) SC - O(1)

        if not head or not head.next:
            return head

        prev = None 
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
