# Binary Tree

## Traversal

- `Pre-order traversal`
  - `Root -> Left -> Right`
  - I try to remember pre-order is the "normal" one so that it starts from room, then left, and finally right
- `In-order traversal`
  - `Left -> Root -> Right`
  - For `binary search tree`, it can retrieve data in sorted order using in-order traversal.
  - I try to remember in-order is to go "in" the tree from left, to root, and to right.
- `Post-order traversal`
  - `Left -> Right -> Root`
  - When you delete a node in a tree, deleting process is post-order
    - i.e. Delete its left child, and its right child, before you delete the node itself.
  - Post-order is used in mathematical expression.
  - I try to remember post-order is something I finally come up with, so (to me) weird left, right, root order.

![LeetCode tree traversal](https://github.com/yukikitayama/leetcode-python/blob/main/image/leetcode_traverse_tree.png)
LeetCode

## Implementation

### Preorder traversal
- [Template](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/binary-tree/preorder_traversal.py) 
- Preorder traversal is DFS, so use stack
- Root should be the first to return, so before DFS to left and right child, append the current value to output
- Although preorder traversal has left before right, push right first to stack before left. 
- But we pop the left first from the top of the stack, so successfully output left first and delay processing right.