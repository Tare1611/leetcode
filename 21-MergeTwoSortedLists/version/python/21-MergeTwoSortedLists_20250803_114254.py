# Last updated: 8/3/2025, 11:42:54 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Approach - Use the tortoise and hare algo, one travels faster than another
        # - If they match then there is a cycle in the linked list.
        # TC - O(n)
        # SC - O(1)

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False