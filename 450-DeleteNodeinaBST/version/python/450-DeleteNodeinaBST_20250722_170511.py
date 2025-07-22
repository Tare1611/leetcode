# Last updated: 7/22/2025, 5:05:11 PM
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Approach  Use dfs recursively, count the outgoing edges 
        # TC - O(n) SC - O(n)

        edges = {(a,b) for a, b in connections}
        neighbors = { city:[] for city in range(n)}
        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visit, changes  #Accessing out of function variables

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes