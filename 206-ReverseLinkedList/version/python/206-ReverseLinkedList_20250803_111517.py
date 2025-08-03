# Last updated: 8/3/2025, 11:15:17 AM
# Repeating the optimal approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach - First check if there is head or not. Next Start reversing the pointer as you progress further.
        # - Have a temporary variable that would store the data for the next node.
        # - Return prev as the start of head
        # TC - O(n) where n is the length of the linked list
        # SC - O(1) since we are using just one variable we can complete in constant space apart from the list itself.

        if not head:
            return None
        
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev