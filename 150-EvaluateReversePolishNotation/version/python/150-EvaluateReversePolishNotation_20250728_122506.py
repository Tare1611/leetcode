# Last updated: 7/28/2025, 12:25:06 PM
# Break the list from middle and reverse the second half, then merge
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Approach - Find the mid and last of the list. 
        # Reverse the second half of the list to traverse correctly and then update the list according to requirement
        # TC - O(n)
        # SC - O(1)

        slow = fast = head
        # Finding the middle and last of the linked list

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the linked list from mid to last

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Merging the two halves

        second = prev
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2