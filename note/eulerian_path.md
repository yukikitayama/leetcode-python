# Eulerian path

- **Eulerian path** in a graph visits every edge exactly once.
- In an undirected graph, either all nodes have an even degree, or exactly two have an odd degree
- In a directed graph, we need to check if
  - Each node's `out_degree` matches its `in_degree`
  - Or, exactly one node has one more outgoing edge (`out_degree = in_degree + 1`), which indicates our starting point
- [2097. Valid Arrangement of Pairs](https://leetcode.com/problems/valid-arrangement-of-pairs/description/)
