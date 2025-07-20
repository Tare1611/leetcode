# Last updated: 7/20/2025, 12:33:20 PM
# Brute Force Approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Brute Force approach - is to use a stack and check with loop in the stack with range n//2
        # TC - O(n) SC - O(n)
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        n = len(stack)
        twin_sum = 0
        max_twin = 0
        
        for i in range(n//2):
            twin_sum = stack[i] + stack[n-1-i]
            max_twin = max(max_twin, twin_sum)

        return max_twin