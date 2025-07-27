# Last updated: 7/26/2025, 7:45:47 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Approach - Assign the number of moves available to a matrix on all cell blocks
        # For start the last row and last column apart from finish will have 1, then start backtracking while adding 

        # TC - O(m*n) SC - O(n)

        row = [1]*n
        
        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]