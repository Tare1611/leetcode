# Last updated: 7/25/2025, 2:35:42 PM
# Have rows to keep the count of moves available
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Approach - Assign the number of moves available to a matrix on all cell blocks
        # For start the last row and last column apart from finish will have 1, then start backtracking while adding 

        # TC - O(m*n) SC - O(m*n)

        row = [1]*n
        
        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]