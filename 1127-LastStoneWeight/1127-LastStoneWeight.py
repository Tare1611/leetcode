# Last updated: 7/31/2025, 6:37:27 PM
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