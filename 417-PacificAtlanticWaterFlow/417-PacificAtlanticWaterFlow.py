# Last updated: 8/4/2025, 5:13:23 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Approach - Use a hash set to store all elements that can reach pacific and atlantic
        # - Go row by row and run a dfs to go through the element and all the position to the element 
        # - 
        # TC - O(n*m)
        # SC - O(n*m)

        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                heights[r][c]< prevHeight):
                return
            visit.add((r,c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result