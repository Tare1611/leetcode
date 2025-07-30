# Last updated: 7/30/2025, 5:58:25 PM
# Using min heap to store the result of Euclidean distance from x,y to 0,0
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Approach - Implement a minHeap to store the distances and the x,y coords. Run a while loop to return the closest
        # TC - O(k * logn)
        # SC - O(n)

        minHeap = []
        for x,y in points:
            dist = (x ** 2)+(y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        result = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x,y])
            k -= 1
        
        return result