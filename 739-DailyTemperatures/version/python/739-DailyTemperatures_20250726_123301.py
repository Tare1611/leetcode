# Last updated: 7/26/2025, 12:33:01 PM
class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.added_back = []
        self.set_back = set()

    def popSmallest(self) -> int:
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.set_back.remove(smallest)
            return smallest
        else:
            self.current += 1
            return self.current - 1

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.set_back:
            heapq.heappush(self.added_back, num)
            self.set_back.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)