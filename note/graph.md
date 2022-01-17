## Graph

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

### Complexity

- Let `V` be number of vertices in a graph, and `E` be the number of the edges.
- Time is `O(V + E)` because it needs to check every vertexa and traverse through every edge in a graph.
- Space is `O(V)` because in the worst case, one vertex is connected to every other vertex, so all of them go to the 
  queue.
