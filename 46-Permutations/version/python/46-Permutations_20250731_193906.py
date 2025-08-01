# Last updated: 7/31/2025, 7:39:06 PM
# Backtracking - Not so optimal
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Approach - Go through the 2-D board and check for the appearance of each letter in the target word.
        # - Use Backtracking since we have to check for the whole word. 
        # TC - O(m * 4^n)
        # SC - O(n)


        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # left, right, down, up
        path = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs (r,c,i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))
            result = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return result
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False