# Graph

- Centroid
  - node that is close to all the peripheral nodes (leaf nodes)
- Tree-alike graph (See tree as a graph) has no more than 2 centroids
  - If the number of nodes is even, there would be 2 centroids.
  - If the number of nodes is odd, there would be 1 centroid.

## Depth first search (DFS)

DFS is used 1. for traversing all the vertices in a graph, and 2. for traversing all the paths between two vertices.

DFS uses recursion call `stack`, LIFO, last in first out.

Often use visited set as helper data structure to avoid visiting the previously visited vertices.

### Complexity
Let V denote the number of vertices, and E the number of edges.
- Traversing all the vertices
  - Time is O(V + E) because it needs to check every vertex
    and traverse through every edge in the graph. 
  - Space is O(V) for the recursion call stack.
- Traversing all the paths
  - Time is O((V - 1)!). -1 because once a path reaches the target, from the target no more traverse occurs. Factorial !
    because, in the worst case, every vertex is connected to every other vertex (Complete graph), meaning that V - 1 
    paths from start to target, V - 2 paths from the next vertex from the start to target, continue...
  - Space is O(V^3), because it comes from O((V(V - 1)/2 + 1) * V). V(V - 1)/2 + 1 comes from (V - 1) paths appended by
    (V - 2) paths, appended by (V - 3), ..., and * V comes from each path added to the stack taking O(V) space (?, need
    review).

### Hierholzer's Algorithm

- `Eulerian path` is a path in a graph that visits every edge exactly once.
- `Eulerian cycle` is an Eulerian path that starts and ends on the same vertex.
- [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

## Breadth First Search (BFS)

- BFS uses `queue`.
- `Sentinel node`
  - Sometimes used in BFS. It's `None` to be inserted to `queue`, and it indicates separation of the levels.
  - e.g. `queue: [1, None, 2, 3, None, 4, ...]` means 2 and 3 are the same level or depth, but 4 is at one level deeper
    different level.
  - When inserting root node to queue, the queue initialization starts from `queue: [root, None]`.
  - But it could be replaced by using the length of the queue. When exhausting nodes at the current level, only pop the 
    number of nodes which are in the current queue.
  - [1602. Find Nearest Right Node in Binary Tree](https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/)

### Complexity

- Let `V` be number of vertices in a graph, and `E` be the number of the edges.
- Time is `O(V + E)` because it needs to check every vertexa and traverse through every edge in a graph.
- Space is `O(V)` because in the worst case, one vertex is connected to every other vertex, so all of them go to the 
  queue.

### Implementation

- Pretty shockingly simple implementation of BFS
  - [Python BFS](https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/99000/Python-BFS)
  - `while any(row)` because the given root could be `None`. `while [None]:` is `True`, but `while any([None])` is 
    `False`

```python
def findValueMostElement(self, root):
    maxes = []
    row = [root]
    while any(row):
        maxes.append(max(node.val for node in row))
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    return maxes
```