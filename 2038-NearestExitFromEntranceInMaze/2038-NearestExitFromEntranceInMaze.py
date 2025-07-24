# Last updated: 7/24/2025, 3:47:55 PM
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Approach - USe bruteforce to traverse all the nearest locations. Use set or mark the visited location. If answer return count else  -1
        # TC - (m*n) SC - O(m*n)
        from collections import deque
        rows = len(maze)
        cols = len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        
        directions = [(-1,0), (0, -1), (1, 0), (0, 1)]

        while q:
            r, c, steps = q.popleft()

            if ( r != entrance[0] or c != entrance[1]) and ( r == 0 or c == 0 or r == rows - 1 or c == cols - 1):
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and  0 <= nc < cols and maze[nr][nc] == ".":
                    q.append((nr, nc, steps + 1))
                    maze[nr][nc] = "+" # Mark visited 
        return -1