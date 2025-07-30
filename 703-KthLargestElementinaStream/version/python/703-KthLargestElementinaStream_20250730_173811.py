# Last updated: 7/30/2025, 5:38:11 PM
# Use minHeap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Approach - Use a maxHeap to store the stones in reverse order, and then compute the stone breaking.
        # TC - O(nlogn)
        # SC - O(n)
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])