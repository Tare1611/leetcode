# Last updated: 7/27/2025, 9:50:57 PM
class TimeMap:

    def __init__(self):
        self.setTimeMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.setTimeMap:
            self.setTimeMap[key] = []
        self.setTimeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.setTimeMap.get(key, [])
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res


# Approach - Store values in set, differentiating according to the key. Get the values according to binary search to return.
# TC - O(logn) for the get, SC - O(m*n)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)