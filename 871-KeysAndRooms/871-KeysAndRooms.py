# Last updated: 7/24/2025, 3:48:07 PM
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Approach - Use bfs to traverse through the room list and store it in set to check
        # TC - O(n + m) n = no. of rooms, m = no. of keys, SC - O(n)
        from collections import deque
        visited = set()
        queue = deque([0])

        while queue:
            room = queue.popleft()
            if room in visited:
                continue
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
        return len(visited) == len(rooms) 