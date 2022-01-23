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
- `Level-order traversal`
  - Use `Breadth First Search (BFS)`
  - use `queue`
- `Morris traversal`
  - Optimize the space complexity to be `O(1)` if excluding the output list
  - Can be applied to all the traversals; preorder, inorder and postorder.
  - [LeetCode animation of Morris preorder traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/solution/)

![LeetCode tree traversal](https://github.com/yukikitayama/leetcode-python/blob/main/image/leetcode_traverse_tree.png)
LeetCode

## Implementation

### Preorder Traversal

- [Template: recursive and iterative approaches](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/binary-tree/preorder_traversal.py) 
- Preorder traversal is DFS, so use stack
- Root should be the first to return, so before DFS to left and right child, append the current value to output
- Although preorder traversal has left before right, push right first to stack before left. 
- But we pop the left first from the top of the stack, so successfully output left first and delay processing right.

### Inorder Traversal

- [Template: recursive and iterative approaches](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/binary-tree/inorder_traversal.py) 

### Postorder Traversal

- [Template: recursive and iterative approaches](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/binary-tree/postorder_traversal.py)
- Append values to a list in preorder traversal in DFS with stack
- Reverse the list to make it the postorder traversal order

### Morris Inorder Traversal

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/solution/)

### Morris Preorder Traversal

- [Template](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/binary-tree/morris_preorder_traversal.py)
- Time is `O(N)`
- Space is `O(1)`

## LeetCode

- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
  - Morris traversal LeetCode solution
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
  - Morris traversal LeetCode solution