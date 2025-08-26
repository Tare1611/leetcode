# Last updated: 8/26/2025, 10:48:32 AM
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False

# Approach - Use a linked list to create implementation of the Hash Set, use a key to store the values
# - Create an array to store all the list nodes for expected number of values in the hash set
# TC - O(N)
# SC - O(N + k) 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)