# Last updated: 8/8/2025, 10:37:13 AM
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Approach - Traverse through the array and store the max gap between 2 seats. 
        # - Return the max gap
        # TC - O(n)
        # SC - O(1)

        n = len(seats)
        start = -1
        maxGap = 0

        for i in range(n):
            if seats[i] == 1:
                if start == -1:
                    maxGap = i
                else:
                    maxGap = max(maxGap, (i - start)//2)
                start = i
        maxGap = max(maxGap, n - 1 - start)
        return maxGap