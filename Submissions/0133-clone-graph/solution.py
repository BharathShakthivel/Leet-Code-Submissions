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
        visited_node = {}
        def dfs(node):
            if node in visited_node:
                return visited_node[node]
            clone = Node(node.val)
            visited_node[node] = clone
            for neigh in node.neighbors:
                clone.neighbors.append(dfs(neigh))
            return clone
        return dfs(node) if node else None
