# Tarjan's algorithm

**Tarjan's algorithm** efficiently finds **articulation points** in a graph. 

**Articulation point** is a cell that will split an island in two when it is changed from land to water.

- **Discovery time**
  - When a node is first visited during the DFS
- **Lowest reachable time**
  - The minimum discovery time of any node that can be reached from the subtree rooted at the current node, including the current node itself.
- **Parent**
  - The node from which the current node was discovered during the DFS

A node can be an articulation point if
- A non-root node is an articulation point if it has a child whose lowest reachable time is greater than or equal to the node's discovery time
  - It means the child and its subtree cannot reach any ancestor of the current node without going through the current node.
  - Meaning the current node is critical for connectivity
- The root node of the DFS tree is an articulation point if it has more than one child.
  - It means removing the root would disconnect these children from each other.

Optimize time

- [1568. Minimum Number of Days to Disconnect Island](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/)
  - Hard