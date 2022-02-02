# Binary Search Tree (BST)

- A special form of a binary tree
- The value in each node is 
  - greater than (or equal to) any values in its left subtree, 
  - and less than (or equal to) any values in its right subtree.
- The strength of a BST is search, insertion and deletion operations are time `O(H)` even in the worst case, where H is 
  the height of a BST.
  - BST is a good choice if we have to handle both insertion and search operations.
- `Inorder traversal` in a BST is in `ascending order`
- `Successor` (node after the current node) is the smallest node after the current node.
- `Predecessor` (node before the current node) is the largest node before the current node.

## Height-Balanced BST (Self-Balancing BST)

- Tree automatically keeps its height small after `insert` and `delete` operations.
- The height of a balanced BST with `N` nodes is always `logN`.
- It also means the height of the two subtrees of every node never differs by more than 1.
  - [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- It matters because BST operations take time proportional to the height of the tree.
- If a BST is skewed, the height is `O(N)`, not `O(H) = O(logN)` where `H` is a tree height.

![LeetCode height balanced BST](https://github.com/yukikitayama/leetcode-python/blob/main/image/leetcode_height_balanced_bst.png)
LeetCode

- There are several implementations of height-balanced BST
  - Red-black tree
  - AVL tree
  - Splay tree
  - Treap

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
- [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)
  - Not obvious from problem statement that we should use BST to solve.
