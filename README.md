# Algorithms in Python and LeetCode

- [daily-challenge](https://github.com/yukikitayama/leetcode-python/tree/main/daily-challenge) folder contains my 
  problem-solving every day by following the daily challenge problems given by LeetCode.
- [algorithm](https://github.com/yukikitayama/leetcode-python/tree/main/algorithm) folder attempts to improve my 
  understanding of a specific algorithms by picking the algorithm from LeetCode.
- [company](https://github.com/yukikitayama/leetcode-python/tree/main/company) folder is a collection of the problems I
  solved with the higher frequency by company.
- [math](https://github.com/yukikitayama/leetcode-python/tree/main/math) folder contains mathematical equations, 
  calculations and proof to get solutions or to calculate complexity.

## LeetCode

LeetCode ID: yukikitayama (https://leetcode.com/yukikitayama/)

### Progress

- [x] Solve 700 LeetCode problems (2021-11-23)
- [ ] Solve 800 LeetCode problems
- [ ] Solve 900 LeetCode problems
- [ ] Solve 1,000 LeetCode problems

### Action

- [ ] Understand Morris Preorder Traversal.

## Dynamic Programming

- There are two ways to implement
  - Bottom-up (Tabulation)
    - Use iteration, by using for loop
    - Start from the base case, save the result in array, and repeat.
    - Usually faster than top-down, because functions calls and cache lookups of top-down are relatively expensive.
  - Top-down (Memoization)
    - Use recursion, by using recursion function.
    - Recursion until it hits the base case, save the result in hashmap, keep until clear the recursion stack.
    - Usually easier to write than bottom-up
- Any DP problem can be implemented and solved with either method.
  - You should be able to do both, because you may be asked to rewrite solution in bottom-up instead if solved in 
    top-down.
- A problem is likely to be a DP problem if ...
  1. Asking for the maximum, minimum, longest, or shortest of something.
  2. Asking for the number of distinct ways to do something (`Counting DP`).
  3. Current decisions depend on previous decisions.
  4. Asking for the path with constraints preventing moving backwards, only allowing to move down and right.
- Without memoization, it's just basic recursion with time O(2^n). But adding memoization makes it DP with time O(N).
- Framework
  1. Identify states
  2. Identify recurrence relation to transition between states.
  3. Identify base case to stop top-down recursion or to start tabulation.
- In multi-dimensional states DP problems, states could be ...
  - Start and end indices `i` and `j`.
  - Numerical constraint `k`. e.g. "You are only allowed to complete `k` transactions".
  - Status in a given state. e.g. "`True` if currently holding a key, `False` if not".
  - Tuple or bitmask indicating "visited" or "used". 
- `functools.lru_cache(maxsize=None)`
  - It means the cache size is not limited. We do this because the number of states that will be re-used in a problem
    is large, and we don't wanna evict a state early and have to re-calculate it.

```python
import functools

def func():
    @functools.lru_cache(maxsize=None)
    def recursion():
        pass
```

- Time and space complexity are the multiplication of states dimentions.
  - State reduction can lower time and space complexity.
- Space optimization
  - Whenever values calculated by DP are reused a few times and not used again, try if it can save space by replacing
    DP array with variables, so space is reduced from O(N) to O(1).
- Counting DP
  - Identify the base cases by logical thinking and usually the base is not 0.

### Kadane's Algorithm

- Find the maximum sum subarray.
- Iterates array and decide whether current index is work keeping or disregard to reset.
- Kadane's Algorithm does not follow the typical DP framework, but it's DP because it uses optimal sub-structures.

#### Complexity

- Time is O(n)
- Space is O(1)

## Math

- Sum of digits time complexity is O(logN), base is 10.
  - https://github.com/yukikitayama/leetcode-python/blob/main/math/sum_of_digits_time_is_logn.png
  - [Explain why time complexity for summing digits in a number of length N is O(logN)](https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn)
- Read an integer one by one from left to right and create number
  - Initialize as `num = 0`, and then in the for loop, `num = num * 10 + curr_num`

### Greatest Common Divisor

- Greatest common divisor of a and b is the largest positive integer d such that d is dividor of both a and b.
  - e.g. gcd(8, 12) is 4. 2 is also common divisor but it's not the largest. 6 is divisor of 12 but 8 is not divisible
    by 6 because divmod(8, 6) is quotient: 1, remainder: 2 not 0.
- Use Euclidean algorithm
  1. Wanna get GCD of `a` and `b`. 
  2. Keep replacing `(a, b)` by `(b, a % b)` until it becomes `(d, 0)`.
  3. `d` is GCD.
- [GCD example](https://github.com/yukikitayama/leetcode-python/blob/main/math/greatest_common_divisor.py)
- Python built-in function `math.gcd` is available from Python 3.5.

### Least Common Multiple

- Least common multiple of a and b is the smallest positive integer that is divisible by a and b.
  - e.g. lcm(4, 6), multiples of 4: 4, 8, **12**, 16, ..., multiple of 6: 6, **12**, 18, ... 12 is the smallest common
    number.
- Use greatest common divisor
  1. Make or import a function to calculate GCD.
  2. `LCM(a, b) = abs(a * b) / gcd(a, b)`.
- [LCM example](https://github.com/yukikitayama/leetcode-python/blob/main/math/least_common_multiple.py)
- Python built-in function `math.lcm` is available from Python 3.9

### Modulo

- Modulo is distributive `(a + b) % n = {(a % n) + (b % n)} % n`
  - LeetCode: [1010. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)
- [Wiki modulo properties](https://en.wikipedia.org/wiki/Modulo_operation#Properties_(identities))

### Remainder

- Numerator is `dividend`. Denominator is `divisor`. Division produces `quotient` and `remainder`.
- Remainder of dividend divided by divisor is equal to the remainder of remainder divided by divisor.
  - e.g. divmod(5, 2) = (2, 1), divmod(1, 2) = (0, 1)
  - [1015. Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/)

### Log

- `log_base(result) = exponent <-> base^exponent = result`
  - `log_2(4) = 2 <-> 2^2 = 4`
- Check whether a number if power of two
  - `if math.log(NUMBER, 2).is_integer()`
    - If NUMBER is 4, it returns 2, which is integer
    - If NUMBER is 3, it returns 1.58..., which is not integer. 
  - `math.log(result, base)`

## Bit Manipulation

### Two's Complement

- To compute two's complement notation -x, revert all bits in x, and add 1
- x = 7: 0 0 0 0 0 1 1 1, ~x: 1 1 1 1 1 0 0 0, ~x + 1: 1 1 1 1 1 0 0 1
- x = 6: 0 0 0 0 0 1 1 0, ~x: 1 1 1 1 1 0 0 1, ~x + 1: 1 1 1 1 1 0 1 0

### Get the Rightmost 1-bit

- `x & (-x)`
  - `-x` is two's complement
- [231. Power of Two](https://leetcode.com/problems/power-of-two/)

| Code | Binary representation |
|------|-----------------------|
| x = 7 | 0 0 0 0 0 1 1 **1** |
| -x = ~x + 1 | 1 1 1 1 1 0 0 **1** |
| x & (-x) | 0 0 0 0 0 0 0 **1** |

### Turn Off the Rightmost 1-bit

- `x & (x - 1)`
  - Subtracting 1 means changing the rightmost 1-bit to 0, and setting all the lower bits to 1, and then 1 & 0 = 0.
- [231. Power of Two](https://leetcode.com/problems/power-of-two/)

| Code | Binary representation |
|------|-----------------------|
| x = 4 | 0 0 0 0 0 **1** 0 0 |
| x - 1 | 0 0 0 0 0 **0** 1 1 |
| x & (x - 1) | 0 0 0 0 0 **0** 0 0 |

### Check Whether a Number is the Power of 2

- `if (x & (x - 1)) == 0`
  - `x` and `x - 1` have different bits in all of their bits, so AND yields 0.

| Action | Binary representation |
|--------|-----------------------|
| x = 4 | 1 0 0 |
| x - 1 = 3 | 0 1 1 |
| x & (x - 1) | 0 0 0 |

### XOR

- Use `A ^ B` in Python
- XOR truth table

| Input A | Input B | Output |
|---------|---------|--------|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

#### Problems

- [67. Add Binary](https://leetcode.com/problems/add-binary/)
- [137. Single Number II](https://leetcode.com/problems/single-number-ii/)
- [260. Single Number III](https://leetcode.com/problems/single-number-iii/)
- [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
- [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)
- [318. Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/)

### 1-bits Bitmask

- In binary representation, all the bits are 1, like `111`.
- To flip bits in a given number

| Action | Binary representation |
|--------|-----------------------|
| Given number: 5 | 1 0 1 |
| 1-bits bitmask | 1 1 1 |
| Number ^ bitmask | 0 1 0 |

- Make 1-bits bitmask
  - Get the number of digits in binary representation of a given number
  - Left-shift 1 the above number of times to give us 1 followed by multiple 0s
  - Subtract 1 to give us all the above 0s become 1s, which is 1-bits bitmask.
- `INTEGER.bit_length()` is a built-in function to get the length of bits or digits.

```python
import math
# Replace num with your given number
num = 5  # 101 in binary representation
number_of_digits = math.floor(math.log2(num)) + 1  # 3
one_bits_bitmask = (1 << number_of_digits) - 1  # 111

# Built-in function
num.bit_length()  # 3
```

### Carry

- `(a & b) << 1`
- AND (`&`) finds the common 1-bit, and left-shift (`<<`) moves the carry to the next bit position

| Action | Binary representation |
|--------|-----------------------|
| a | 1 1 1 1 |
| b | 0 0 1 0 |
| (a & b) << 1| 0 1 0 0 |

### Create a binary number from the most significant bit

- `(previous bit << 1) | current bit`
  - e.g. Previous bit: 1, current bit: 1, the result needs to be 11, which is 3 in binary representation.
  - `1 << 1` gives us `10`. `10 | 1` gives us `11`. It's 3.
- `previous digit * 10 + current digit` is the equivalent in decimal representation
  - e.g. Make 12, previous digit: 1, current digit: 2, 10 + 2 = 12

## Probability and Statistics

### Reservoir Sampling

- Sample one or more elements from an unknown size population with equal probability and constant space.
- Equal probability is obtained by `prob to be chosen * prob to stay * prob to stay * ...` in the iteration.
- [Reservoir sampling math](https://github.com/yukikitayama/leetcode-python/blob/main/math/reservoir_sampling.png)
- [382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/)

## Amortized Analysis

- Gives the average performance of each operation in the worst case.
- The worst case operation can alter the state in such a way that the worst case cannot occur again for a long time
  ("amortizing cost").

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

- Consider heap when asked for getting top-k elements from list.
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

## Divide and Conquer

- Big picture
  1. Divide the problem into two or more subproblems until these are simple enough to solve.
  2. Conquer by solving each subproblem recursively.
  3. Combine the results of each subproblem.
- If you do not combine subproblmes and if instead use a single smaller subproblem, it's `decrease and conquery` such as
  Binary Search.

### Master Theorem

- `Master Theorem (Master Method)` calculates the time complexity of the recursion algorithms with divide and conquer.
- `a`: The number of subproblems needed to be solved
- `b`: The number of subproblems made by dividing a problem
- `d`: Complexity parameter for dividing and combining
  - `d = 0` if dividing and combining is constant
- `f(n)`: Time complexity to divide a problem into subproblems adn to combine the results from the subproblems.
  - If dividing and combining is constant, `f(n) = O(1) = O(n^0) with d = 0`
  - `f(n) = O(n^d)`
- `T(n)`: Time complexity of divide and conquer recursion
  - `T(n) = a * T(n / b) + f(n)`. This will further be converted into the followings by `a`, `b`, and `d`.
    - `T(n) = O(n^(log_b(a)))` if `a > b^d`
      - e.g. DFS in binary tree `O(n)`
    - `T(n) = O(n^d * log(n)) = O(n^(log_b(a)) * log(n))` if `a = b^d`
      - e.g. Binary search `O(log(n))`
    - `T(n) = O(n^d)` if `a < b^d`
- DFS to traverse every node in the binary tree
  - `a = 2` because DFS needs to traverse both left and right child
  - `b = 2` because each node in binary tree splits into left and right child
  - `d = 0` because binary tree data structure allow DFS to traverse in constant
  - `b^d = 2^0 = 1, less than a, so a > b^d, so T(n) = O(n^(log_b a)) = O(n^(log_2 2)) = O(n^1) = O(n)`
- Binary search
  - `a = 1` because binary search cuts a problem into half, so only one of the subproblems needed to be solved
  - `b = 2` because binary search divides a problem into halves
  - `d = 0` because dividing is constant by using middle index, and no need to combine because it simply returns the
    result of subproblem without further processing.
  - `b^d = 2^0 = 1, equal to a, so a = b^d, so T(n) = O(n^d * log(n)) = O(n^0 * log(n)) = O(log(n))`
- Limitations
  - Master Theorem only applies to the cases where the subproblems are of equal size.
    - e.g. not applicable to the recursion for Fibonacci number which divides into two subproblems of different sizes.
- Math: [Proving the Master Theorem](https://www.youtube.com/watch?v=I7JCtSwVeXs)

### Merge Sort

- Sort algorithm by using divide and conquer.
  - [Template: top-down merge sort](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/recursion/top_down_merge_sort.py)
- Big picture
  1. Divide the unsorted list into sublists
  2. Sort each sublist recursively
  3. Merge sorted sublists to make a new sorted list
- Time is `O(NlogN)` because dividing takes N times to get a single element, merging repeats N elements times on each 
  level, and it has logN levels.
- Space is `O(N)` because it needs to keep sublists and buffer to hold the merge results.

### Quick Sort

- Sorting algorithm using divide and conquer.
  - [Template: quick sort]()
- Pick a pivot value to divide a list into two sublist, until reach the base case, and recursively sort.
- Time
  - `O(NlogN)` in the best case and on average.
    - When the pivot value happends to be median value of the list, and each partition divides into two equal size 
      sublists.
    - It results in a balanced binary search tree with height `logN`. At each level, scanning takes `O(N)`
  - `O(N^2)` in the worst case
    - If pivot value is smallest or largest, partition divides the list into one single sublist and the other empty 
      list.
    - Partitioning occur `N` times, and each partition scans `N` elements.

## Backtracking

- Find every possible patterns or ways
- If we are only interested in the number of patterns or ways, consider using dynamic programming, because generating 
  every possible patterns is time-consuming.

## Trie

- If you are asked to dynamically add and search strings.
- Usually it's implemented as nested hashmaps.
- Template: [Trie Python code](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/trie/Trie.py)

### LeetCode

- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

## Greedy

- The idea of greedy algorithm is to pick the locally optimal move at each step, and it will lead to the globally 
  optimal solution.
- Greedy problem usually look like "Find minimum number f something to do something" or "Find maximum number of 
  something to fit in some condition", and typically propose an unsorted input

#### Problem

- [134. Gas Station](https://leetcode.com/problems/gas-station/)
- [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## Deterministic Finite Automation (DFA)

- `State machine` reads some input and changes the states based on those inputs.
- `Transition` is the change in a state.
- `Finite state machine` is the state machine with a finite number of states.
- `Deterministic finite automation (DFA)` is the finite state machine that either `accept` or `reject` a sequence of
   states.
  - e.g. Traffic light. "Green -> Yellow -> Red -> Green" are accepted each time in the sequence. But "Green -> Yellow
    -> Red -> Yellow" is rejected when Red changes into Yellow.
- There is only one path for the specific input from the current state to the next state.

#### Problem

- [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
- [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
- [65. Valid Number](https://leetcode.com/problems/valid-number/)
- [520. Detect Capital](https://leetcode.com/problems/detect-capital/)
- [890. Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)
- [1018. Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/)

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

## Stack

- Use stack when you wanna delay processing the current data later

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

- Inorder traversal
  - `Left -> Root -> Right`
- Preorder traversal
  - `Root -> Left -> Right`
- Postorder traversal
  - `Left -> Right -> Root`
- [All DFS traversals (preorder, inorder, postorder) in Python in 1 line](https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line)

### Morris Preorder Traversal

- Morris preorder traversal is constant space for DFS preorder traversal in binary tree, while recusrive and iterative
  DFS use `O(H)` space where `H` is the height of the binary tree.
  - Recursion uses recursion stack for `O(H)`
  - Iteration uses queue for `O(H)`

#### Problem

- [1022. Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)

## Decision Tree

- A special form of binary tree used in classification and regression.
- Decision node
  - Non-leaf node.
  - Each decision node contains a condition as a branching rule.
    - Less-then-or-equal comparison
    - Membership of category
- Each leaf node contains a label assigned to objects which fall into this leaf.
- Stopping condition
  - All the data fall into a node belong to the same category.
  - The tree reaches the predefined maximum depth.
  - The number of examples fall into a node is less than the predefined minimum number of data in a node.


## Binary Search Tree (BST)

- Inorder traversal of a binary search tree gives nodes in the ascending order.
- Inorder is `left -> root -> right`.

### Example

- Problems to solve by using BST properties
  - [669. Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)

## Linked List

- `Singly linked list` contains value and a reference field to link to the next node, but no link to the previous node.
  - Cannot trace back the previous node, so the algorithm needs to store both current and previous nodes.
- `Doubly linked list` has `next` and `prev` field.
  - Delete is `O(1)` time and space unlike singly linked list, because no need to traverse.
- Two pointers technique (`prev` and `curr`, or `fast (hare)` and `slow (tortoise)`) often works for solution to 
  traverse the linked list.
  - Sometimes need `prev` because singly-linked list does not have a reference to the precedent node.
  - Check if a node is null before it calls the next field, otherwise it causes the null-pointer error.
  - Don't forget to define the end conditions in two pointers iteration loop.
- `Sentinel node` is a dummy pseudo head or tail node in linked list to standardize linked list algorithm, doesn't hold
  any meaningful data.
  - [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
- Benefit of linked list over array
  - In linked list, inserting an element is `O(1)` time because it only updates reference to next node. But in array,
    it takes `O(N)` time because it needs to move all elements after the inserted element.
  - If it needs to add or delete a node frequently, linked list is better.
  - If it needs to access an element by index, array is better.

| Action | Position | Array | Single linked list | Doubly linked list |
|--------|----------|-------|--------------------|--------------------|
| Access | By index | O(1) | O(N) | O(N) |
| Add | Before head | O(N) | **O(1)** | **O(1)** |
| Add | After given position | O(N) | **O(1)** | **O(1)** |
| Add | After tail | O(1) | O(N) | **O(1)** |
| Delete | Head | O(N) | **O(1)** | **O(1)** |
| Delete | Given position | O(N) | O(N) | **O(1)** |
| Delete | Tail | O(1) | O(N) | **O(1)** |
| Search | Given val | O(N) | O(N) | O(N) |

### Floyd's Tortoise and Hare (Floyd's cycle-finding algorithm)

- Detect cycle in linked list.
- Benefit of using this algorithm is
  1. Time is linear time `O(N)`
  2. Space is `O(1)` because it only uses two pointers to reference of linked lists.
- Algorithm
  - Find the intersection node by hare moving 2 nodes and tortoise moving 1 node.
  - Make two pointers
    - Pointer 1 starts from the intersection node
    - Pointer 2 starts from the head of linked list
    - Iterate both pointers one by one
    - Two pointers will be identical at the entrance of the cycly in the linked list.
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
- [Python code](https://github.com/yukikitayama/leetcode-python/blob/main/company/goldman-sachs/gs_142_linked_list_cycle_ii_2.py)



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

## Sort

### Timsort

- Python `LIST.sort()` and `sorted(LIST)`.
- Time is `O(NlogN)`.
- Space is `O(N)`

### Counting sort

- Suitable when the value range of array is not significantly greater than the length of array.
- Algorithm
  - Initialize array with 0s with length (max - min + 1)
  - Get shift by -min
  - Iterate each num in the given array
  - Count up the initialized array at current num + shift
- Complexity
  - Let N be the length of the given array, and M be the value range of the array.
  - Time is `O(M + N)` because initializing the array is `O(M)` and iterating the given array is `O(N)`.
  - Space is `O(M)` for the initialized array.

#### Example

- [1200. Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)

### Bucket Sort

- Sorting algorithm that works by distributing the elements of an array into a number of buckets
- Require prior knowledge for the range of the data
- Useful if you know the range of values from the problem constraints.
- For example, initialize an empty array by the length by min and max of the value range, insert the original array 
  value as the index to the new array, so you don't need to apply sort, because when inserting, values are sorted.

#### Example

- [1094. Car Pooling](https://leetcode.com/problems/car-pooling/)
- [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)

### Quickselect

- Should consider whether Quickselect can be applied when the problem is to find the k (or kth) smallest/larest/etc 
  element(s).

#### Example

- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

## Recursion

- Solve problems using a functions that calls itself.
- `Base case (bottom case)` is the case where one can compute the answer directly without any further recursion calls.
  - Something to stop recursion.
- `Execution tree` is used to find time complexity in recursion
  - Each node represents recursive function call.
  - Total number of nodes in the tree is the number of recursion calls, which is time complexity.
- `Stack overflow` is where the stack allocated for recursion reaches its maximum space limit and the program crashes. 
- Space allocated by the recursion stack
  - Returning address of function call, i.e. the line of code to return after a function call is completed.
  - Parameters passed to the function call
  - Local variables in the function call
- `Tail recursion` is a recursion where the recursive call is the final instruction in the recursion function, no other 
  computations at the end of the function, and there should be only one recursive call in the function.
  - Benefit of tail recursion is that it allows to `reuse a fixed amount space` in the recursion stack to save space by 
    avoiding accumulating the stacks.
  - So tail recursion is used to avoid `stack overflow`.
  - Tail recursion also makes things easier to read and understand, compared to non-tail-recursion.
  - It doesn't need a call stack for all the recursive calls, because, as soon as it returns from a recursive call, 
    immediately go to return to the original caller.
  - Non-tail-recursion functions are not automatically optimized by Python and Java. But C and C++ recognizes tail 
    recursion pattern and automatically optimizes the execution.
    - [Optimizing tail-recursion in Python](https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion)

```python
def tail_recursion(nums):
    def recursion(nums, accumulator):
        if len(nums) == 0:
            return accumulator
        # recursion() is a tail recursion 
        # because the final instruction is only a recursive call
        return recursion(nums[1:], nums[0] + accumulator)
    return recursion(nums, 0)

def not_tail_recursion(nums):
    if len(nums) == 0:
        return 0
    # not_tail_recursion() is not a tail recursion 
    # because it needs to add the result of recursion to nums[0] as an extra computation,
    # so the final instruction is not only a recursive call
    return nums[0] + not_tail_recursion(nums[1:])
```

## Python Swap

- Reduce a temporary variable and lines of code by multiple items at the both sides of an equal sign.

```python
# Before
tmp = curr.next
curr.next = prev
prev = curr
curr = tmp

# After
curr.next, prev, curr = prev, curr, curr.next
```

## String

- `STRING.split()` time complexity is `N` where `N` is the length of the string.
  - [Time/space complexity of in-built python functions](https://stackoverflow.com/questions/55113713/time-space-complexity-of-in-built-python-functions)
- `Substring` is a **contiguous** sequence of characters within a string.

### Rabin-Karp Algorithm

- Pattern searching
  - e.g. Plagiarism detection, similar protein search in bioinformatics.
- Idea
  - Allows algorithm to compute the hash of the pattern string and substring by sliding window in the given string.
  - Pattern matching becomes computing two hashes and compare, which makes the time constant.
  - Rolling hash also makes the recomputing of the hash in the next sliding window the constant time.
- Time is `O(n + m)` where `n` is the length of the given string, and `m` is the pattern length.
- Worst case time is `O(n * m)`. Worst case of Rabin-Karp algorithm occurs when all characters of pattern and text are same as the hash values of all
  the substrings of the given string match with hash values of the pattern
  - e.g. The given string: "AAAAAAA", pattern: "AAA"
- [Rolling Hash Function Tutorial, used by Rabin-Karp String Searching Algorithm](https://www.youtube.com/watch?v=BfUejqd07yo)

#### Problem

- [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)
- [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)

## Array

- `Subsequence`
  - An array by deleting some or no elements without changing the order of the remaining elements
  - e.g. `[3, 6, 2, 7]` is a subsequence of the array `[0, 3, 1, 6, 2, 2, 7]`.
- `enumerate(iterable, start)` can change the starting integer by start.

```python
input = ['a', 'b', 'c']
print(list(enumerate(input)))
# [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(enumerate(input, 1)))
# [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(enumerate(input[1:], 1)))
# [(1, 'b'), (2, 'c')]
```

## Iterator

- Only needs to know how to get the next item.
  - It doesn't need to store the entire data in memory.
- It can represent a sequence without using a data structure
  - Below, if min and max are far apart, an array data structure allocates a lot of memory
  - But the RangeIterator still consumes only `O(1)` space
```python
class RangeIterator:
    def __init__(self, min, max):
        self.current = min
        self.max = max

    def has_next(self):
        return self.current < self.max

    def next(self):
        # This updates self.current
        self.current += 1
        # This does not update self.current
        return self.current - 1
```

- Can handle an infinite sequence. An array is always bounded finite sequence.

### Problem

- [284. Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)

## Set

- `SET.discard(ITEM)` doesn't raise an error if the specified item does not exist in the set, while `SET.remove(ITEM)`
  raises an error.

## Resource

- [Stable Sort](https://www.youtube.com/channel/UCV2g02zq5y7unJ_GSr-de2w/videos)

## Game

- [Snake game](https://en.wikipedia.org/wiki/Snake_(video_game_genre))
  - [Play online](http://patorjk.com/games/snake/)

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
