# HashSet

## Concept

- `Separate chaining` is a way for values with the same hash key to keep in a bucket.
  - Storage this hashset is an array, and each element in the array is the bucket.
  - Given a value, generate a key via hash function, use the generated key to find the bucket.
- Common choice of `hash function` is `modulo` operator.
  - `Hash = value % base`
  - `Base` determines the number of buckets. `Prime number` is used.
  - More buckets, less collisions
- HashSet will be optimized for time if each bucket uses a Binary Search Tree.
  - If each bucket uses array, search and delete takes `O(N)` for the for loop
  - But with BST, the time becomes `O(logN)` because in each iteration, search space gets half.
  - But we need to implement `search`, `insert`, and `delete` operations of BST by ourselves.

## LeetCode

- [705. Design HashSet](https://leetcode.com/problems/design-hashset/)

To review BST operations

- [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
- [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)