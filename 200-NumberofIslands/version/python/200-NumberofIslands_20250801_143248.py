# Last updated: 8/1/2025, 2:32:48 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach - Select first instance and work through the matrix, check for horizontal and vertical location. 
        # - Mark adjacent 1's and the original one as visited to not go through that value again
        # - Use BFS to check for the adjacent 1's
        # TC - O(m*n)
        # SC - O(m*n)
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0


        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[-1,0], [1,0], [0,1], [0,-1]] # left, right, up, down

                for dr, dc in directions:
                    r, c= row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == "1"
                        and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands