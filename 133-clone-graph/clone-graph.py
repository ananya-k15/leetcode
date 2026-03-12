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
        # edgecase: empty graph
        if node is None:
            return None

        # create a seenNodes hashmap to track node val : newNode
        seenNodes = dict()

        # helper function: cloneNode
        def cloneNode(node):
            # for every node in org graph p
            # check if we've already cloned p
            if node.val in seenNodes.keys():
                # if yes, return seenNodes[p]
                return seenNodes[node.val]
            # if no, clone p and add it to the seenNodes hashmap
            newNode = Node(node.val, [])
            seenNodes[node.val] = newNode
            # for all neighbours of p
            if node.neighbors is not None:
                for n in node.neighbors:
                    # call cloneNode and assign the result to the list
                    newNode.neighbors.append(cloneNode(n))
                    # m = cloneNode(n)
                    # if newNode.neighbors is None:
                    #     newNode.neighbors = [m]
                    # newNode.neighbors = newNode.neighbors + [m]
            return newNode

        # call cloneNode on the first node
        # return the deep copy 
        return cloneNode(node)

        