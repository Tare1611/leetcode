# Last updated: 7/28/2025, 11:02:49 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach - Binary Search the 2-D Array 
        # TC - O(log(m*n))  SC - O(1)
        rows = len(matrix)
        cols = len(matrix[0])
        lrow = 0 
        rrow = rows - 1

        while lrow <= rrow:
            mrow = (lrow+rrow)//2

            if target in matrix[mrow]:
                lcol = 0
                rcol = cols - 1

                while lcol <= rcol:
                    mcol = (lcol + rcol)//2

                    if matrix[mrow][mcol] == target:
                        return True
                    elif matrix[mrow][mcol] < target:
                        lcol = mcol + 1
                    else:
                        rcol = mcol - 1
            elif matrix[mrow][cols-1] > target:
                rrow = mrow -1
            else:
                lrow = mrow +1
        return False