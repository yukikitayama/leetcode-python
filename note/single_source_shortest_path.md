## Single Source Shortest Path

### Dijkstra's Algorithm

- Solve the shortest path problem in a weighted directed graph with **non-negative** weights.
- It's a greedy approach because each step selects minimum weights from the current vertex to find the shortest path to
  other vertex.
- Dijkstra's algorithm won't work if there's a negative edge somewhere in the graph, because greedy algorithm looking 
  only at the current vertex with others does not work.

#### Complexity

- Time is O(E + V * logV) because it takes O(E) to consider all the edges to find minimum weights, and takes O(VlogV)
  to get minimum element from the min heap.
- Space is O(V) because it needs to store all the vertices min distance and previous vertex information.

### Bellman-Ford Algorithm

- Solve the shortest path problem in a weighted directed graph with any weights including negative weights.
- Bellman-Ford Algorithm is based on Dynamic Programming and optimizes the space.
  - If there's a restriction to use at most k edges, Bellman-Ford Algorithm needs to be implemented by DP.
- But Bellman-Ford Algorithm cannot calculate the shortest path in **graph with negative-weight cycle**, because it 
  doesn't exist.
- Suppose a graph has a cycle with weights, and the sum of the weights is positive, call it the graph with 
  positive-weight cycle, and if the sum of weight is negative, the graph with negative-weight cycle.
  - In the graph with positive-weight cycle, there's the shortest path, because by cycling, the total weight keeps 
    increasing.
  - In the graph with negative-weight cycle, there's the shortest path, because, by cycling, the total weight keeps
    decreasing.

#### Shortest Path Faster Algorithm (SPFA algorithm)

- Improvement of Bellman-Ford algorithm.
- Use a queue to maintain the next starting vertex.
- Add a vertex only when it updates the shortest path to the vertex and the vertex is not in the queue.
- Iterate until the queue is empty.

#### Complexity

- Bellman-Ford Algorithm in Dynamic Programming implementation
  - Time is O(V * E). In the worst case, all the vertices are connected with each other, so it needs to check every edge
    from every vertex.
  - Space is O(V^2) because it needs to make 2 dimensional DP table with the number of edges at most axis and the 
    to-vertex axis.
- SPFA Bellman-Ford Algorithm
  - Time is O(V * E). In the worst case, SPFA is the same as the standard Bellman-Ford algorithm, but on average, SPFA
    tends to be faster.
  - Space is O(V)
