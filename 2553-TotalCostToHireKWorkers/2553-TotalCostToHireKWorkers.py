# Last updated: 7/24/2025, 10:23:37 PM
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Approach - Maintain 2 priority queues and work with K values, and also track total cost
        # TC - O(k logn) SC - (candidates)
        heap = []
        total_cost = 0
        for i in range(candidates):
            heapq.heappush(heap, (costs[i],i))
        front_end = i  
        back_end = max(front_end + 1, len(costs)-candidates)
        for j in range(back_end, len(costs)):
            heapq.heappush(heap, (costs[j],j))
            
        while k > 0:
            cost, i = heapq.heappop(heap)
            total_cost += cost
            k -= 1
            if front_end < back_end - 1:
                if i <= front_end:
                    front_end += 1
                    heapq.heappush(heap, (costs[front_end], front_end))
                else:
                    back_end -= 1
                    heapq.heappush(heap, (costs[back_end], back_end))
        return total_cost
        