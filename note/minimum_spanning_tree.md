# Minimum spanning tree

- **Spanning tree** is a subgraph in a graph where all the vertices are connected with the minimum number of edges. 

- **Minimum spanning tree** is a spanning tree with the minimum total edge weight. 

- Spanning tree is in an undirected graph, and minimum spanning tree is in a weighted undirected graph. Those graphs could
have multiple (minimum) spanning trees.

- **Cut** is a partition of vertices in a graph into two disjoint subsets. 
  - Cut has **crossing edges** which connect a vertex in one disjoint subset with another vertex in the other disjoint 
    subset. 
  - Among the crossing edges, if you choose the edge with the smallest weight, it belongs to minimum spanning tree. This
    is called **cut property**.

### Kruskal's algorithm

An algorithm to make a minimum spanning tree of a weighted undirected graph.

Kruskal's algorithm expands minimum spanning tree by adding edges.

#### Algorithm
1. Sort a list of edges in the ascending order by weight.
2. Add an edge in the order to minimum spanning tree.
   - Skip the current edge if it makes a cycle.
3. Repeat until N - 1 edeges are added. 
   - N - 1 because, if it's more than N - 1, it has too many edges to be spanning tree.

#### Complexity
Time is O(E * logE), because sorting edges take O(E * logE), and for each edge, checking whether two vertices belong to 
the same connected component take O(E * &alpha;(V)), so O(E * logE + E * &alpha;(V)) = O(E * logE). &alpha;() is the 
inverse ackerman function.

Space is O(V), because it needs union find data structure to keep track of the root of every vertex.

### Prim's Algorithm

Another algorithm to make a minimum spanning tree of a weighted undirected graph.

**Cut propety** works for the newly added edges described below. There are edges which connect two disjoint set, which
are cut. Picking the minimum weight edge among then connect two disjoint set as minimum spanning tree.

Prim's algorithm expands the minimum spanning tree by adding vertices.

#### Algorithm

1. Make an empty visited set, and a non-visited set initially containing all the vertices.
2. Remove a vertex from the non-visited, and find the minimum weight edge out from the vertex to an unvisited vertex.
3. Remove the chosen vertex, treat this connected vertices as a whole, find the minimum weight edge out from the whole
   to an unvisited.
4. Repeat until N - 1 edges picked.

#### Complexity

- Time is O(E * logV) with binary heap. O(V + E) to traverse all the vertices and store them in the heap. Getting 
  minimum element from the heap costs O(logV), so O(V + E) * O(logV) = O(E * logV)
- Space is O(V) to store all the vertices.

## LeetCode

- [1135. Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/description/)
  - Medium
- [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
  - Medium
- [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/)
  - Hard
  - Kruskal's Algorithm