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
