# Last updated: 7/16/2025, 8:15:15 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force approach use two for loops and traverse the list. Getting TLE in large length
        # TC - O(n^2) SC - O(1)
        # area = 0
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = min(height[i], height[j]) * (j-i)
        #         max_area = max(max_area, area)
        # return max_area
        # Trying to optimise - Use 2 pointers have a single loop traverse from both start and end
        # TC - O(n) SC - O(1)
        n = len(height) - 1
        left = 0
        right = n
        max_area = 0
        area = 0
        while left < right:
            area = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

