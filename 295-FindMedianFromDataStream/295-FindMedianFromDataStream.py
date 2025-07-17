# Last updated: 7/16/2025, 8:14:47 PM
class MedianFinder:

    def __init__(self):
        # self.stream = []
        self.low = []   # max-heap (invert sign)
        self.high = []  # min-heap

    def addNum(self, num: int) -> None:
        # self.stream.append(num)
                # Add to max-heap
        heapq.heappush(self.low, -num)

        # Balance: move largest in low to high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Rebalance if needed: low can have more elements
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
        

    def findMedian(self) -> float:
        # sorted_stream = sorted(self.stream)
        # n = len(sorted_stream)
        # if n % 2 == 1:
        #     return float(sorted_stream[n//2])
        # else:
        #     mid1 = sorted_stream[n//2-1]
        #     mid2 = sorted_stream[n//2]
        #     return (mid1 + mid2)/2 
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()