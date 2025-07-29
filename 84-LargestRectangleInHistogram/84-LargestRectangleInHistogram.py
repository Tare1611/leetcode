# Last updated: 7/28/2025, 11:02:47 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Approach - Have a stack and store the index and height
        #  - keep track of max_area before popping the greater height if we encounter a smaller height
        #  - update the index of the smaller to previous one
        # TC - O()
        # SC - O()

        stack = [] #pair of elements [index, heights]
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height*(i - index))
                start = index
            stack.append([start,h])
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area