# Last updated: 7/16/2025, 8:15:13 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute Force Approach - Use a while loop to find length of the list. and then second for loop to reach till 'n'
        # TC - O(l) SC - O(1)
        # length = 0
        # curr = head

        # while curr:
        #     length += 1
        #     curr = curr.next
        
        # if length == n:
        #     return head.next

        # curr = head
        # for _ in range(length - n - 1):
        #     curr = curr.next
        
        # curr.next = curr.next.next
        # return head
        
        # Trying Optimal Approach using two pointers
        
        dummy = ListNode(next = head)
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next