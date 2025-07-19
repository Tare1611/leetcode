# Last updated: 7/19/2025, 12:29:22 PM
'''
Brute Force Approach - convert the grid with rows to grid columns and then use nested for loop to check for same values
TC - O(n^2) SC - O(n)
'''

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        print(row)
        print(col)

        grid_col = list(map(list, zip(*grid)))
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid_col)):
                if grid[i] == grid_col[j]:
                    count += 1


        print(grid_col)
        return count