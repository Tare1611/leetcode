# Last updated: 7/24/2025, 2:49:29 PM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Approach - Use Binary Search to go through the values.
        # TC - O(logn) SC - O(1)

        n = len(arr)
        l = 0 
        r = n - 1
        mid = 0

        while l < r:
            mid = (l + r) //2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l
