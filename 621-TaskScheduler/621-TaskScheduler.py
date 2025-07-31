# Last updated: 7/31/2025, 6:37:42 PM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Approach - Use the most frequent tasks first and then work with the condition
        # TC - O(n)
        # SC - O(n)

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time