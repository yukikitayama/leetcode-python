## Topological Sorting

- A linear sorting based on the required ordering between vertices in directed acyclic graphs.
- For example, `u -> v`, in topological sorting, `u` has to appear before `v`.

### Kahn's Algorithm

- Find **in-degree** and **out-degree** for each vertex. 
  - Make an adjacency list with key a vertex, and value a list of vertices which are prerequisite of the key vertex.
- Add a vertex when its in-degree becomes 0.
- Decrease in-degree of each vertex when it finds a vertex pointing at (prerequisite).
- When a queue is empty, it stops
- In **cyclic graph**, this algorithm does not work, because there's no node with in-degree 0.

#### Complexity

- Time is O(V + E), because making the adjacency list takes O(E), and in the worst case, it needs to visit every vertex
  and decrement every outgoing edge once to take O(V + E).
- Space is O(V + E), because the adjacency list is O(E), queue is O(V) at most.
