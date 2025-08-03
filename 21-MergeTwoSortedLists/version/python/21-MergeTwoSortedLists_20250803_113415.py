# Last updated: 8/3/2025, 11:34:15 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach - Traverse through the both the linked list and select the value that is small to go first.
        # - If same then take the first value fromm any of the list - for me '1'
        # - If one list ends then attach the next list at the end
        # TC - O(n+m) Length of list 1 and list 2
        # SC - O(1)

        if not list1 and not list2:
            return None
        
        result = ListNode(0, None)
        curr = result

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        
        
        curr.next = list1 or list2
        
        return result.next