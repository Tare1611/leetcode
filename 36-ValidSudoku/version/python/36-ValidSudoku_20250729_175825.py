# Last updated: 7/29/2025, 5:58:25 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Approach - detect the duplicates using Hash set and Hash Map.
        # TC - O(n^2) SC - O(n^2)

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  #key = (r/3, c/3) 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
