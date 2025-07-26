# Last updated: 7/25/2025, 7:50:41 PM
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Approach - Consider the balloons as intervals, and find the max list of overlapping.
        # TC - O(n)  SC - O(n)
        points.sort()

        result = len(points) # Max num of arrows if no overlap
        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]

            if curr[0] <= prev[1]:
                result -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr
        return result