# Last updated: 7/31/2025, 6:37:31 PM
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