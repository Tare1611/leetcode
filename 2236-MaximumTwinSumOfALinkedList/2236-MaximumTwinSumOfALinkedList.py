# Last updated: 7/20/2025, 8:15:31 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Brute Force approach - is to use a stack and check with loop in the stack with range  n//2
        # TC - O(n) SC - O(n)
        # stack = []
        # curr = head

        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        
        # n = len(stack)
        # twin_sum = 0
        # max_twin = 0
        
        # for i in range(n//2):
        #     twin_sum = stack[i] + stack[n-1-i]
        #     max_twin = max(max_twin, twin_sum)

        # return max_twin

        # Optimal Approach - Work through the linked list find middle element and then work with sum
        # TC - O(n) SC - O(1)
        if not head and not head.next:
            return head
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # work max_twin
        max_twin = 0
        first = head
        second = prev
        while second:
            max_twin = max(max_twin, first.val + second.val)
            first = first.next
            second = second.next
        return max_twin
