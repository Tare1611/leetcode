# Last updated: 7/16/2025, 8:15:06 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        # Brute Force - Use while loop and just go through the integers and find the closest i for square
        # TC - O(n) SC - O(1)
        # i = 0
        # while i*i <= x:
        #     i += 1
        # return i - 1

        # Optimal Approach - Use binary search divide the search area in half and test the midpoint.
        # TC - O(log x) SC - O(1)
        left = 0
        right = x
        result = 0
        while left <= right:
            mid = (left + right)//2
            if mid * mid <= x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result