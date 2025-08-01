# Last updated: 8/1/2025, 5:04:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach - Traverse through the lists and calculate the sum, carry forward the tens value if any, return the final answer in list
        # TC - O(m + n) - trying to finish in linear time
        # SC - O(1)
        
        answer = ListNode()
        curr = answer
        carry = 0
        unit = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            unit = total % 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr.next = ListNode(unit)
            curr = curr.next
        return answer.next