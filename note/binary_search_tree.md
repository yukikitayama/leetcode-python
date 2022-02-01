# Binary Search Tree (BST)

- A special form of a binary tree
- The value in each node is 
  - greater than (or equal to) any values in its left subtree, 
  - and less than (or equal to) any values in its right subtree.
- The strength of a BST is search, insertion and deletion operations are time `O(H)` even in the worst case, where H is 
  the height of a BST.
- `Inorder traversal` in a BST is in `ascending order`
- `Successor` (node after the current node) is the smallest node after the current node.
- `Predecessor` (node before the current node) is the largest node before the current node.

## Operation

### Search

- Return the current node if the target value is equal to the current node value.
- Keep searching the left child if the target value is less than the current node value
- Keep searching the right child if the target value is greater than the current node value
- The above can be implemented either recursively or iteratively.

### Insertion

- Compare the current node value and the new node value to decide to go left or right.
- Repeat until reaching a leaf
- Add the new node as left or right child depending on the leaf node value and the new node value
- So every new node starts from the root, and added as a new leaf.

### Deletion

- Go down the left or right, depending on the target and current value, until it finds the target node
- If it finds a target
  - If it doesn't have left and right, just make the target node None
  - If it has the right child, find the `successor` in the right, replace the current node with the successor value, and
    delete the original successor in the right
  - If it has the left child, find the `predecessor` in the left, replace the current node with the predecessor value, 
    and delete the original predecessor in the left
- Find `successor`, the next smallest node after the current one.
  - Go to the right once, and then go to the left as many times as you can
- Find `predecessor`
  - Go to the left once, and then go to the right as many times as you can
- [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

## Complexity

- Let `H` be the height of a BST.

### Search

- Time is `O(H)` either with recursion or iteration.
- Space is `O(1)` with iteration because discarding the half, while `O(H)` with recursion because the system stack is 
  used.

### Insertion

- Time is `O(H)` typically either recursion or iteration.
- But in the worst case where a tree is skewed with each child at the same side, time is `O(N)`.
- Space is, with recursion `O(H)` but `O(N)` in the worst case for the system stack.
- With iteration space is `O(1)`.

## Problem

- [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
  - Need to understand how to find predecessor and successor in BST.
