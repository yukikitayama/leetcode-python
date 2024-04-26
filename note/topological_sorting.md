# Topological Sorting

- A linear sorting based on the required ordering between vertices in directed acyclic graphs.
- For example, `u -> v`, in topological sorting, `u` has to appear before `v`.

## Kahn's Algorithm

- Find **in-degree** and **out-degree** for each vertex. 
  - Make an adjacency list with key a vertex, and value a list of vertices which are prerequisite of the key vertex.
- Add a vertex when its in-degree becomes 0.
- Decrease in-degree of each vertex when it finds a vertex pointing at (prerequisite).
- When a queue is empty, it stops
- In **cyclic graph**, this algorithm does not work, because there's no node with in-degree 0.

### Complexity

- Time is O(V + E), because making the adjacency list takes O(E), and in the worst case, it needs to visit every vertex
  and decrement every outgoing edge once to take O(V + E).
- Space is O(V + E), because the adjacency list is O(E), queue is O(V) at most.

## LeetCode

- [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)
- [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/description/)
- [1136. Parallel Courses](https://leetcode.com/problems/parallel-courses/)
- [1203. Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/)
- [2115. Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)
- [2204. Distance to a Cycle in Undirected Graph](https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/description/)