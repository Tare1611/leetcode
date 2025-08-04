# Last updated: 8/4/2025, 2:30:21 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Approach - Similar to count of islands, just use a counter to keep a track of the islands in one connected pass.
        # - Use bfs to traverse and then return the max area value
        # TC - O(n*m)
        # SC - O(n*m)

        if not grid:
            return 0 
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0


        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [1,0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r,c) not in visited):
                        q.append((r, c))
                        visited.add((r,c))
                        area += 1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    # bfs(r,c)
                    max_area = max(max_area, bfs(r, c))
                    # islands += 1
        return max_area

