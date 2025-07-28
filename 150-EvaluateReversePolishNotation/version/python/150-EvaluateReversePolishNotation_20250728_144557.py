# Last updated: 7/28/2025, 2:45:57 PM
# Create a new linked list storing the output and keep in mind the carry
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
        list1 = l1
        list2 = l2
        curr = answer
        tens = 0 #carry
        unit = 0
        while list1 or list2 or tens:
            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0
            tot = v1 + v2 + tens
            tens = tot // 10
            unit = tot % 10
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
            curr.next = ListNode(unit)
            curr = curr.next
        
        return answer.next