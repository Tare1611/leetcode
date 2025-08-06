# Last updated: 8/6/2025, 11:44:24 AM
# Use dfs and hash map to store values
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Approach - Perform DFS on each node and store the outcome in a Hash Map, with a value for safe. 
        # - If there is a cycle the node is not safe. 
        # - If a node reaches only a safe node then it is safe node.
        # - If there are no outgoing nodes then the node is safe.
        # TC - O(n)
        # SC - O(n)
        
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            else:
                safe[i] = False
                for nei in graph[i]:
                    if not dfs(nei):
                        return safe[i]
                safe[i] = True
                return safe[i] 

        result = []
        for i in range(n):
            if dfs(i):
                result.append(i)
        return result