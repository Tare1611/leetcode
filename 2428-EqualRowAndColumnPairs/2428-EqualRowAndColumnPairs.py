# Last updated: 7/19/2025, 3:55:20 PM
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Brute Force Approach - Have an extra list of the grid arr in col format using zip, and then use nested for loop to check
        # TC - O(n^3) SC - O(n^2)
        
        # row = len(grid)
        # col = len(grid[0])
        # print(row)
        # print(col)

        # grid_col = list(map(list, zip(*grid)))
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid_col)):
        #         if grid[i] == grid_col[j]:
        #             count += 1


        # print(grid_col)
        # return count

        # Optimal Approach - Use tuple and hashing to improve TC
        # TC - O(n^2) SC - O(n^2)
        from collections import Counter

        n = len(grid)
        row_counter = Counter(tuple(row) for row in grid)
        
        count = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += row_counter[col]
        return count
