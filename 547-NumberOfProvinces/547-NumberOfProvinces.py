# Last updated: 7/24/2025, 3:48:12 PM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Approach - Use dfs and a set to hold the number of visited room. We are given adjacency matrix so easy to find connected.
        # TC - O(n^2) SC - O(n)
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)


        n = len(isConnected)
        visited = set()
        provinces = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces
