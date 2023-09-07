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
        if not node:
            return
        
        store = {}
        visited = set()
        queue = deque([])
        queue.append(node)

        while queue:
            cur = queue.popleft()
            visited.add(cur.val)
            print(f"visited: {visited}")
            new = store.get(cur.val)
            if not new:
                new = Node(val=cur.val)
                store[cur.val] = new
            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
                new_neighbor = store.get(neighbor.val)
                if not new_neighbor:
                    new_neighbor = Node(val=neighbor.val)
                    store[neighbor.val] = new_neighbor
                if new_neighbor not in new.neighbors:
                    new.neighbors.append(new_neighbor)
        return store[1]
        