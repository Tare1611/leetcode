# Last updated: 7/28/2025, 11:02:50 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #  Approach - Have an extra row and col to the end and right of the grid.
        # Do a bottom up calculation of the path, return res[0][0] as answer.
        # TC - O(n*m)
        # SC - O(n*m)

        rows = len(grid)
        cols = len(grid[0])

        result = [[float("inf")] * (cols + 1) for r in range(rows + 1)]
        result[rows-1][cols] = 0

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                result[r][c] = grid[r][c] + min(result[r + 1][c], result[r][c + 1])
        return result[0][0]