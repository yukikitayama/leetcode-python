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

### Deletion

- Deleting from the end of array is `O(1)` time
- Deleting from the start of array is `O(N)` time, because to fill the deleted spot, it needs to shift every element all
  the way to the last by one place to the left.
- Deleting from the middle is `O(N)` time, because it needs left shift of every element to the right

## Linear Search

- The way for finding an element by checking through all elements one by one
- Time is `O(N)`

## LeetCode

- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
  - Easy level problem, but it requires thinking to optimize space complexity