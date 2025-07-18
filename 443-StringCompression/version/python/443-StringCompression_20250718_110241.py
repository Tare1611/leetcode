# Last updated: 7/18/2025, 11:02:41 AM
# Two pointer approach - keep track of area
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force approach use two for loops and traverse the list. Getting TLE in large length
        # TC - O(n^2) SC - O(1)
        # n = len(height)
        # area = 0
        # max_area = 0
        # for i in range(n):
        #     area = 0
        #     for j in range(i+1, n):
        #         area = min(height[i], height[j]) * (j-i)
        #         max_area = max(max_area, area)
        # return max_area

        # Need Optimal solution since TLE
        # TC - O(n) SC - O(1)
        n = len(height) - 1
        l = 0 
        r = n
        area = 0
        max_area = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
