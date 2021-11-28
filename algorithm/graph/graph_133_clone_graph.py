"""
Result
- Start: 11:34
- End: 11:43
- Saw solution: 1
- Optimized: 1
- Solved: 1

Complexity
- Time is O(V + E) because it needs to traver every vertex through every edge
- Space is O(V) for the hashmap and recursion call stack
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        # Assume that neighbors is list of Node objects if not none, otherwise []
        self.neighbors = neighbors


class Solution:
    def __init__(self):
        # Hashmap with key the reference to the original node,
        # and value the reference to the cloned node
        self.original_to_clone = {}

    def cloneGraph(self, node: 'Node') -> 'Node':

        if node in self.original_to_clone:
            return self.original_to_clone[node]

        # We could have empty graph input. In this case, node does not have .val
        # , so cloning node make error. So if node is Node, stop the algorithm
        if not node:
            return node

        # Clone the given node
        clone_node = Node(node.val, [])

        # Make the current node as visited, and record original node and cloned node connection
        self.original_to_clone[node] = clone_node

        if node.neighbors:
            # self.cloneGraph() returns cloned node,
            # so clone_node.neighbors will be a list of cloned node
            clone_node.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]

        # clone_node is an object of cloned node
        return clone_node


