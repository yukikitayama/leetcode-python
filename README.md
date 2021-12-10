# Algorithms in Python and LeetCode

- [daily-challenge](https://github.com/yukikitayama/leetcode-python/tree/main/daily-challenge) folder contains my 
  problem-solving every day by following the daily challenge problems given by LeetCode.
- [algorithm](https://github.com/yukikitayama/leetcode-python/tree/main/algorithm) folder attempts to improve my 
  understanding of a specific algorithms by picking the algorithm from LeetCode.
- [company](https://github.com/yukikitayama/leetcode-python/tree/main/company) folder is a collection of the problems I
  solved with the higher frequency by company.
- [math](https://github.com/yukikitayama/leetcode-python/tree/main/math) folder contains calculations to get solutions or to calculate complexity.

## LeetCode

LeetCode ID: yukikitayama (https://leetcode.com/yukikitayama/)

### Progress

- [x] Solve 700 LeetCode problems (2021-11-23)
- [ ] Solve 800 LeetCode problems
- [ ] Solve 900 LeetCode problems
- [ ] Solve 1,000 LeetCode problems

## Dynamic Programming

- There are two ways to implement
  - Bottom-up (Tabulation)
    - Use iteration, by using for loop
    - Start from the base case, save the result in array, and repeat.
    - Usually faster than top-down
  - Top-down (Memoization)
    - Use recursion, by using recursion function.
    - Recursion until it hits the base case, save the result in hashmap, keep until clear the recursion stack.
    - Usually easier to write than bottom-up
- Any DP problem can be implemented and solved with either method.
- A problem is likely to be a DP problem if ...
  1. Asking for the maximum, minimum, longest, or shortest of something.
  2. Current decisions depend on previous decisions.

## Minimum spanning tree

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

## Heap

- Efficiently access the largest or smallest element in the data.
- Heap is a data structure, while priority queue is an abstract data type.
  - Heap is a way to implement priority queue, which can be implemented by array and linked list.
  - Heap implementation of priority queue is time O(logN) for insertion and deletion
  - Linked list implementation of priority queue is time O(1) for insertion and deletion, but other operations O(N)
- Heap is a complete binary tree, and each node value must be no greater than (or no less than) the child node values
  - Max heap has the largest value at the top, and min heap has the smallest at the top.
- Max heap
  - Python heapq is min heap, so multiplying -1 makes it max heap.
  - Top element is still the smallest element in the heap, but when taking out an element, multiply -1 again to get back
    the original value.
```python
import heapq

# Construct max heap
max_heap = [1, 2, 3]
max_heap = [-x for x in max_heap]
heapq.heapify(max_heap)

# Insert an element to max heap
heapq.heappush(max_heap, -1 * 4)

# Get the top element
-1 * max_heap[0]

# Delete the max element
heapq.heappop(max_heap)

# If you need to use the popped element
value = -1 * heapq.heappop(max_heap)
```
- To get the K-th **smallest** element, there are two ways to implement
  - Put all the N elements to **min** heap and pop K elements from the top.
    - Time is O(KlogN + N) because O(N) to make the min heap, and O(logN) to pop for k elements.
  - Put each element to **max** heap one by one. If the heap has k elements and the current element is bigger than or 
    equal to the top element, continue. If the current element is smaller than the top element, insert it to the max 
    heap, and pop the top element. Because it's max heap, the top element is the largest element in the heap. But this
    approach limits the size of the heap, so the largest element is actuall k-th smallest element.
    - For example, K is 2, and to find the 2nd smallest element, max heap only contains 2 elements, the bottom of the 
      heap is the smallest element and top is the 2nd smallest element, because the heap only contains 2 elements.
    - Time is (NlogK), because, in K size element, inserting and deleting is O(logK) and do this for each N elements.
  - So optimal solution depends on N and K.

### Method

- Insert
  - Add a new node to the bottom leftmost position to keep complete binary tree
  - Keep exchanging the node with the parent node until parent value is smaller than child value (Min heap)
- Delete
  - Remove the top element.
  - Move the bottom rightmost node to the top to keep complete binary tree.
  - Keep exchanging the node with the children until parent and child value satisfy the min heap or max heap condition.

### Complexity

- Insert
  - Add a new node at the bottom, and in the worst case, it compares the node with all the parent nodes from bottom to 
    top. So time is the height of the tree
  
- Time
  - Constructor is O(N)
  - Insert is O(logN). LogN because at most exchanging needs to run the tree height times. Tree height is LogN
  - Delete is O(logN)
  - Get max or min (Get the top element) is O(1)
  - Get heap size is O(1)
- Space
  - Constructor is O(N)
  - Insert is O(1)
  - Get max or min is O(1)
  - Get heap size is O(1)

### Implementation

- Array
  - [Min heap template](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/heap/MinHeap.py)
  - Size is heap size + 1. +1 because of the convenience and not use the element at 0 index.
    - The element at index 0 in the array could store the number of elements in the heap. 
  - Find a parent node by `n // 2`.
  - Find the left and right children by `left = n * 2` and `right = n * 2 + 1`.
  - Find whether the current index is a leaf node by `i > (n // 2)`

### Heap Sort

#### Algorithm

- Input is array
- Make a complete binary tree from the array
- Heapify it, meaning keeping complete binary tree and making min or max order by exchanging non-leaf nodes with 
  parents and children.
- Pop the top element and insert it to the result sorted array.
- Move the bottom rightmost element to the top, and exchange with children to maintain min or max structure.
- Repeat all the elements

#### Complexity

- Time
  - O(N * logN), because making the array to min or max heap is O(N), popping each element is O(N), and moving the 
    bottom rightmost to top and exchanging is O(logN) for operating within tree height, so O(N * logN).
- Space
  - O(N) for the heap.

### Top k smallest/largest problem

#### Algorithm

- Add all the elements in the array to heap
- Popping the top element, adding to a result array, exchanging the bottom rightmost elements k times.

#### Complexity

- Time
  - O(k * logN), because making heap is O(N), and popping top element and keeping heap structure is O(k * logN), and we 
    consider O(k * logN) is bigger than O(N).
- Space
  - O(N) because it still adds all the N elements to heap.

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

## Trie

- If you are asked to dynamically add and search strings.
- Usually it's implemented as nested hashmaps.
- Template: [Trie Python code](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/trie/Trie.py)

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

## Tree

- An undirected graph in which any two vertices are connected by exactly one path
- Any connected graph without cycles is a tree.

## Binary Tree

- Recursion template. Key is to implement `if node is None` for how to end the recursion.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(node, other_information):
    if node is None:
        return 'Things like 0 or None'
    else:
        'Do something relates to helpe(node.left) and helper(node.right)'

def answer_to_problem(root):
    return helper(root, 'other_information')
```

- Postorder traversal
  - `Left -> Right -> Root`

## Binary Search Tree (BST)

- Inorder traversal of a binary search tree gives nodes in the ascending order.
- Inorder is left, root, right.

## Linked List

- two pointers (`prev` and `curr`) iteration often works for solution to traverse the linked list.
  - Because singly-linked list does not have a reference to the precedent node.

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

### LeetCode

- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

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
