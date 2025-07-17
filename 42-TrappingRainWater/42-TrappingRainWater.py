# Last updated: 7/16/2025, 8:15:09 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force Apporach - Use for loop and traverse through the array to identify the spaces available by doing right - left.
        # TC - O(n^2) since using Max function inside the for loop, SC - O(n)

        # n = len(height)
        # total = 0
        # for i in range(n):
        #     left = max(height[:i+1])
        #     right = max(height[i:])
        #     total += min(left, right) - height[i]
        # return total

        # Optimal Approach 1 - Generate the max left amd right values a store in array and then move ahead with the min calculation.
        # TC - O(n), SC - O(n)

        n = len(height)
        if n==0:
            return 0

        total = 0
        left = [0]*n
        right = [0]*n

        left[0] = height[0]
        for i in range(1,n):
            left[i] = max(left[i-1], height[i])
        
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        for i in range(n):
            total += min(left[i], right[i]) - height[i]
        return total

