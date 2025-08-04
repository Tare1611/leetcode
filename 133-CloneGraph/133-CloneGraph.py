# Last updated: 8/4/2025, 5:13:48 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Approach - Use a hashmap to store the node values traversed and, recursively go through the graph
        # - Check for the values in hashmap and create a new graph 
        # - return the copy node 
        # TC - O(V + E)
        # SC - O(V)
        oldToNew = {}
        if not node:
            return None
            
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)