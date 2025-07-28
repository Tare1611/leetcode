# Last updated: 7/28/2025, 1:45:38 PM
# Two pass approach - One to create hashmap of deep copy and other to link them
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Approach - Two passes needed, create a hash map of the nodes and then in the second pass update the links
        # TC - O(n)
        # SC - O(n)

        oldToCopy = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        # Second Pass to set the pointers
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]     