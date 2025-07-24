# Last updated: 7/24/2025, 3:47:15 PM
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Approach 3 binary searches, first to find peak, second to check left, and third to check right
        # TC - O(logn) SC - O(1)

        n = mountainArr.length()
        l = 1
        r = n - 2
        mid = 0
        peak = 0
        while (l <= r):
            mid = (l + r)// 2
            ml = mountainArr.get(mid-1)
            mm = mountainArr.get(mid)
            mr = mountainArr.get(mid+1)

            if ml < mm < mr:
                l = mid + 1
            elif ml > mm > mr:
                r = mid - 1
            else:
                break
        peak = mid

        # Searching left of peak

        l = 0
        r = peak

        while l <= r:
            mid = (l+r)//2
            val = mountainArr.get(mid)

            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid

        # Searching right of peak

        l = peak
        r = n-1

        while l <= r:
            mid = (l+r) // 2
            val = mountainArr.get(mid)

            if val < target:
                r = mid - 1
            elif val > target:
                l = mid + 1
            else:
                return mid

        return -1

