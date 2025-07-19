# Last updated: 7/19/2025, 3:55:19 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force approach - loop through list to find the length, then calc middle and create a dummy list for removal
        # TC - O(n) SC - O(1) 2 loops but not nested
        length = 0
        if not head or not head.next:
            return None
        
        curr = head
        while curr:
            length += 1
            curr = curr.next

        mid = length // 2
        curr = head
        for _ in range(mid - 1):
            curr = curr.next
        curr.next = curr.next.next

        return head

        # Optimal Approach - Use two pointers fast and slow
        # TC - O(n) SC - O(1) Single loop

        if not head or not head.next:
            return None
        
        fast = slow = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next

        return head