# Last updated: 7/19/2025, 2:37:02 PM
from collections import deque
class RecentCounter:                               
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
        
# Approach - Use queue to store the values and update when t-3000 not present
# TC - O(1) as per ping call updates are there. SC - O(W) ping window in time frame

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)