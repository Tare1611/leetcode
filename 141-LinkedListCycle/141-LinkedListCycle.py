# Last updated: 7/16/2025, 8:14:58 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute Force Approach - Use a set to store values and iterate
        # TC - O(n), SC - O(n)
        # visited = set()
        # while head:
        #     if head in visited:
        #         return True
        #     visited.add(head)
        #     head = head.next
        # return False
        # Optimal Approach - Use two pointer approach fast and slow
        # TC - O(n), SC - O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False