# Last updated: 8/22/2025, 4:39:59 PM
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Approach - Traverse through the matrix and check for the first 1 from top and last one from bottom
        # - Once we find the bounding points we get the rectangle area
        # TC - O(m*n)
        # SC - O(m*n)

        rows = len(grid)
        cols = len(grid[0])

        mxx = mxy = 0
        mnx = mny = float('inf')

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    mxx = max(mxx, i)
                    mnx = min(mnx, i)
                    mxy = max(mxy, j)
                    mny = min(mny, j)
        return (mxx - mnx + 1) * (mxy - mny + 1)