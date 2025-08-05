# Last updated: 8/5/2025, 9:40:20 AM
# Using minHeap to store x, y and dist
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Approach - Calculate the distance from origin and store it in a minHeap to get the smallest distance first
        # - Run a while loop till k == 0 and return the result array with just x and y coords.
        # TC - O(n) - will run 2 loops.
        # SC - O(n) - to store the min heap and then result

        minHeap = []

        for x, y in points:
            dist = (x**2 + y**2)**0.5
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        result = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x,y])
            k -= 1
        return result
        