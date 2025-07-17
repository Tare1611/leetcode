# Last updated: 7/16/2025, 8:15:10 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force Approach - Collect all nodes and sort them
        # TC - O(nlogn) SC - O(n) - Creating a node array with all the values
        # nodes = []

        # while list1:
        #     nodes.append(list1.val)
        #     list1 = list1.next

        # while list2:
        #     nodes.append(list2.val)
        #     list2 = list2.next

        # nodes.sort()

        # dummy = ListNode()
        # curr = dummy

        # for val in nodes:
        #     curr.next = ListNode(val)
        #     curr = curr.next
        # return dummy.next

        # Trying to speed up and optimize the solution merging inplace, using pointers
        # TC - O(n) SC - O(1)

        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return  dummy.next
