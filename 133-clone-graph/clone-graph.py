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
        if node is None:
            return None
        
        stack = [node]
        seen = {}

        while stack != []:
            n = stack.pop()
            if n not in seen:
                seen[n] = Node(n.val)
            for x in n.neighbors:
                if x not in seen:
                    stack.append(x)
                    xCopy = Node(x.val, [])
                    seen[x] = xCopy
                seen[n].neighbors.append(seen[x])

        return seen[node]

                    

