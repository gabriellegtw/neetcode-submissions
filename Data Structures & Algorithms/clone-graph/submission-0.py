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
        if not node:
            return None

        queue = deque()
        visited = {}

        # Put the first node in
        queue.append(node)
        visited[node] = Node(node.val)
        
        # While queue is not empty
        while len(queue) != 0:
            # Get current node
            curr = queue.popleft()

            for n in curr.neighbors:
                if n not in visited:
                    # Add to visited
                    visited[n] = Node(n.val)
                    queue.append(n)

                neighbor_copy = visited[curr].neighbors
                neighbor_copy.append(visited[n])

        return visited[node]
        