# Last updated: 8/4/2025, 9:00:08 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Appraoch - First check for the unsurrounded regions and Replace the "O" with Temp value
        # - Then perform nested for loop for the capture task to capture all the "O" surrounded by "X"
        # - Convert the unsurrounded to "O"
        # TC - O(n*m)
        # SC - O(n*m)

        ROWS = len(board)
        COLS = len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                board[r][c] != "O"):
                return
            board[r][c] = "T"
            # Traverse all 4 directions of r and c 
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # DFS to capture unsurrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r,c)


        # Capturing the surrounded regions

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Return the temp to "O" on unsurrounded regions

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        