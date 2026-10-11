"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        new_node = Node(val = node.val, neighbors = [])
        visited = {node: new_node}
        todo = deque([(node, visited[node])])
        

        while len(todo) > 0:
            original, copy = todo.popleft()

            for neighbor in original.neighbors:
                if neighbor in visited:
                    copy.neighbors.append(visited[neighbor])
                else:
                    visited[neighbor] = Node(val = neighbor.val, neighbors = [])
                    copy.neighbors.append(visited[neighbor])
                    todo.append((neighbor, visited[neighbor]))
        
        return new_node

        