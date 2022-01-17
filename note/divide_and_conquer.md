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
