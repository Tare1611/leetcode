# Last updated: 7/16/2025, 8:14:52 PM
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
        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        # curr = head
        # while curr:
        #     curr.val = stack.pop()
        #     curr = curr.next
        # return head
        # Optimal Approach - Iteratively travel and reverse the list
        # TC - O(n), SC - O(1)
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev