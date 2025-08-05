# Last updated: 8/5/2025, 3:41:42 PM
# Repeat
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Approach - Have a stack and store the index and height
        # - Also keep a track of the area by new bars that allow extension of previous bar height
        # - If a new bar comes in with height lower than current, pop that element 

        # TC - O()
        # SC - O()

        maxArea = 0
        stack = [] #pair of index and height

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea