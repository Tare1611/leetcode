# Last updated: 8/1/2025, 6:00:37 PM
# 2 pointer approach move which is small
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

        # Optimal Approach 1 - Generate the max left amd right values a store in array and then move ahead with the
        # - Move inside from the side with min height.

        # TC - O(n), SC - O(n)

        l = 0
        r = len(height) - 1

        if not height:
            return 0

        leftMax = height[l]
        rightMax = height[r]
        total = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
        return total