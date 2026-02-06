# Last updated: 2/5/2026, 8:47:52 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        # Approach - Start with 2 variables Units and Digits
9        # Keep a track of the linked lists and then if one ends append the other
10        # Have a final result linked list as well.
11        # TC -
12        # SC - 
13        digit = 0
14        carry = 0
15
16        dummy_list = ListNode()
17        curr = dummy_list
18
19        while l1 or l2 or carry:
20            a = l1.val if l1 else 0
21            b = l2.val if l2 else 0
22            add = a + b + carry
23            carry = add // 10
24            unit = add % 10
25
26            curr.next = ListNode(unit)
27            curr = curr.next
28            l1 = l1.next if l1 else None
29            l2 = l2.next if l2 else None
30        
31        curr.next = l1.next if l1 else None
32        curr.next = l2.next if l2 else None
33        return dummy_list.next
34