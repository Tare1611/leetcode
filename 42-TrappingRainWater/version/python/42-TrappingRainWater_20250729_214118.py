# Last updated: 7/29/2025, 9:41:18 PM
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

        if not height:
            return 0

        result = 0
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        return result
