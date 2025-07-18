# Last updated: 7/18/2025, 10:54:44 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force Approach - 2 for loops, keep track of area
        # TC - O(n^2), SC - O(1)
        # n = len(height)
        # max_area = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         area = min(height[i] , height[j]) * (j-i)
        #         max_area = max(max_area, area)
        # return max_area
        # Optimal Approach - Use 2 pointer to reduce running time
        # TC - O(n), SC - O(1)
        n = len(height)
        max_area = 0
        left, right = 0, n-1
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
