# Last updated: 7/29/2025, 9:03:07 AM
# Use a mergeFunc to merge two linked list, run the loop to go through the list of linked list with 2 step forward
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Approach - Use the principle of Merge Sort. Merge 2 sorted linked list
        # TC - O(nlogk) - n is length of linked list, with k list
        # SC - O()

        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeFunc(l1, l2))
            lists = mergedLists
        return lists[0]

    # function to merge list
    def mergeFunc(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2: 
            tail.next = l2
        return dummy.next
