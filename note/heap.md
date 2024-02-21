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

## N largest

If you can remember the following, solving will be fast. `T: O(NlogK)`.

```pytho
import collections
import heapq

counter = collections.Counter(something)
k = integer

heapq.nlargest(k, counter.keys(), key=counter.get)
```

- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
