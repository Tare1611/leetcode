# Last updated: 7/24/2025, 3:48:04 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Approach - Use BFS to traverse throught the matrix, check for adjacent values and update counter
        # TC - O(n * m) SC - O(n * m)
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Add all rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh += 1
        # print(queue)
        # print(fresh)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        minutes = 0

        # Step 2: BFS
        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # rot it
                    fresh -= 1
                    queue.append((nr, nc, time + 1))
        # print(queue)
        # print(fresh)
        return minutes if fresh == 0 else -1

