# Algorithms in Python and LeetCode

- [daily-challenge](https://github.com/yukikitayama/leetcode-python/tree/main/daily-challenge) folder contains my 
  problem-solving every day by following the daily challenge problems given by LeetCode.
- [algorithm](https://github.com/yukikitayama/leetcode-python/tree/main/algorithm) folder tried to improve my 
  understanding of a specific algorithms by picking the algorithm from LeetCode.
- [company](https://github.com/yukikitayama/leetcode-python/tree/main/company) folder is a collection of the problems I
  solved with the higher frequency by company.

## LeetCode

LeetCode ID: yukikitayama (https://leetcode.com/yukikitayama/)

### Progress

- [x] Solve 700 LeetCode problems (2021-11-23)
- [ ] Solve 800 LeetCode problems
- [ ] Solve 900 LeetCode problems
- [ ] Solve 1,000 LeetCode problems

## Hash table

When you use modulo as hash function, the divisor should use prime number (e.g. 1999), because it can best avoid 
collision.

Integer, string and tuple are the Python valid dictionary keys. You cannot use list as key, because Python list is 
[mutable unhashable object](https://www.geeksforgeeks.org/how-to-use-a-list-as-a-key-of-a-dictionary-in-python-3/). So first convert the list to tuple, and then use it as a key of the Python dictionary.

### Complexity

In the best case, the bucket size is small enough to be regarded as constant, so insertion and search are O(1). But in 
the worst case, all the items go to the same bucket and the size becomes N, so search time complexity will be O(N) while
insertion is still O(1).

If there are too many values in the same bucket, you should use `height-balanced binary search tree` instead. In the 
worst case, search and insertion time complexity is O(logN).

## Disjoint set
Disjoint set = union-find. The goal is 1. to find whether two vertices share a common ancestor, and 2. connect two 
vertices. Disjoint set is optimized by implementing union by rank and path compression. Implementation of Disjoint set
is highly modularized, so it's good to just memorize the implementation of disjoint set with union by rank and path
compression.

Template: [Disjoint Set Python code](https://github.com/yukikitayama/leetcode-python/blob/main/disjoint-set-union-find/DisjointSet.py)

Union by rank is to limit the maximum height of each vertex to improve find() time complexity. Find the height (rank) of
the root nodes and choose the bigger rank root node as the root node in union().

Path compression is to update a parent node with a root node in find() to improve find() time complexity by avoiding
taking O(N) every time in calling find().

### Method
- find(vertex)
  - Find the root node of a given vertex.
- union(vertex1, vertex2)
  - Connect two vertices by making their root nodes the same.

### Complexity
- Optimized disjoint set with union by rank and path compression
  - Constructor is O(N) to make parent array and rank array.
  - find() is O(alpha(N)), where alpha() is the Inverse Ackermann function
    - O(alpha(N)) is regarded as O(1) on average.
  - union() is O(alpha(N))
  - Space is O(N) for the two arrays.
- Quick find
  - Parent array stores root vertex, not parent vertex.
  - For time, find() is O(1), but union() is O(N) because it needs to iterate parent array to update root node.
  - Space is O(N) for the parent array.
- Quick union
  - find() keep searching root node while a parent of the current node is not the current node.
  - union() uses either the found root node as a parent. The root is found by find().
  - Both find() and union() takes O(logN)
  - Quick union is more efficient than quick find, because to union all the nodes, quick find takes N * O(N) union, 
    but quick union takes less than or equal to N * O(N) because find() of quick union updates root nodes.

### Terminology
- Parent node
  - The direct parent node of a vertex. For example, 0 (Root) - 1 - 3, The parent node of 3 is 1.
- Root node
  - A node without a parent node. In the above example, 0 is a root node.

## YouTube

LeetCode Number | Problem Name | Level | YouTube | Language
--------------- | ------------ | ----- | ------- | --------
21 | Merge Two Sorted Lists | Easy | https://youtu.be/5J_iUgDQqow | English
105 | Construct Binary Tree from Preorder and Inorder Traversal | Medium | https://youtu.be/Q9xtzCxzpSg | English
729 | My Calendar I | Medium | https://youtu.be/OoKST96zFdo | Japanese
695 | Max Area of Island | Medium | https://youtu.be/9FtAC0yPigQ | English
102 | Binary Tree Level Order Traversal | Medium | https://youtu.be/9fmXC3lyDCw | Japanese
359 | Logger Rate Limiter | Easy | https://youtu.be/Npj5zJj8C2s | English
323 | Number of Connected Components in an Undirected Graph | Medium | https://youtu.be/LXh35C1hVQA | Japanese
204 | Count Primes | Easy | https://youtu.be/HwXK1DJIf1k |
326 | Power of Three | Easy | https://youtu.be/iHTOFDlkJqg |
1480 | Running Sum of 1D Array | Easy | https://youtu.be/HbSN-ElXHwc |
