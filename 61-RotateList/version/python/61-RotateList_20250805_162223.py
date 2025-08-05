# Last updated: 8/5/2025, 4:22:23 PM
# Optimal O(n) approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Approach - First get the length of the linked list
        # - Next calculate the pivot point of the linked list
        # - Traverse till the point and break the list and attach the last node's pointer from length loop to the current head
        # Return the new head
        # TC - O(N)
        # SC - O(1)

        if not head:
            return head
        
        # Finding the length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1
        
        # Finding the pivot point
        k = k % length
        if k == 0:
            return head
        
        # Reaching the pivot and updating the list
        curr = head
        for i in range(length - k - 1):
            curr = curr.next

        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead