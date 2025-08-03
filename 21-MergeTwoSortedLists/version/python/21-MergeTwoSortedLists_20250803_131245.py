# Last updated: 8/3/2025, 1:12:45 PM
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
        # Approach - Do a mid partition to the list and reverse the second half of the list.
        # - Then combine the list from both partition, accoridng to the conditions given.
        # TC - O(n)
        # SC - O(1)



        # Finding mid and last of the list
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        # Reversing the second half of the linked list
        mid = slow.next
        prev = slow.next = None

        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        # Merging the 2 halves
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        