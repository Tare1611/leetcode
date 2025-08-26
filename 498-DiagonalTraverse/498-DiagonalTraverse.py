# Last updated: 8/26/2025, 10:48:48 AM
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Approach - From the start we go one col and row up and right
        # - When we reach out of bounds, go in reverse so down and left
        # - Repeat the same till you reach the last element
        # TC - O(m * n)
        # SC - O(m * n)

        rows = len(mat)
        cols = len(mat[0])
        result = []
        curr_row = 0
        curr_col = 0
        go_up = True

        while len(result) != rows * cols:
            if go_up:
                while curr_row >= 0 and curr_col < cols:
                    result.append(mat[curr_row][curr_col])
                    curr_row -= 1
                    curr_col += 1
                
                if curr_col == cols:
                    curr_col -= 1
                    curr_row += 2
                else:
                    curr_row += 1
                go_up = False
            else:
                while curr_row < rows and curr_col >= 0:
                    result.append(mat[curr_row][curr_col])

                    curr_col -= 1
                    curr_row += 1 
                if curr_row == rows:
                    curr_row -= 1
                    curr_col += 2
                else:
                    curr_col += 1
                go_up = True
        return result
                
