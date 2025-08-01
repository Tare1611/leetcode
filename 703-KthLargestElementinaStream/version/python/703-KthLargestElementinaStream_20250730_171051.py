# Last updated: 7/30/2025, 5:10:51 PM
# Use of minHeap to return the kth largest element
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
  
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
# Approach - We can use a minHeap of size(k) to store the numbers in the heap, pop the element if more.
# - Return the Kth largest number in the list given which can have addition in the list. 
# - Other approach is sort the list every time there is addition is done to the list but it is slow


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)