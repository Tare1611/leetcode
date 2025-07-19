# Last updated: 7/19/2025, 3:42:17 PM
# Use while loop to calculate length and for loop to reach till middle - 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force approach - loop through list to find the length, then calc middle and create a dummy list for removal
        # TC - O() SC - O(n)
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
