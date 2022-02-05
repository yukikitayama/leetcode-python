# Array

- When solving an array problem in-place, should consode 

## Operation

### Append

- Appending an element at the end of an array is `O(1)` time
- `LIST.append(ELEMENT)`

### Insertion

- Inserting an element at any given index is `O(N)` time, because first it needs to move all the other element to the 
  right of the index one step to right, and insert a new element to the empty space at the index.
- `LIST.insert(INDEX, ELEMENT)`

## LeetCode

- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
  - Easy level problem, but it requires thinking to optimize space complexity