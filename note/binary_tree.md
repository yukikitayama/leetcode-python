# Binary Tree

## Traversal in Binary Tree

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

- [All DFS traversals (preorder, inorder, postorder) in Python in 1 line](https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line)

## Construct Binary Tree from Traversal

- Preorder traversal array has a root at the first element.
- Postorder traversal array has a root at the last element.
- Inorder traversal array can split into left and right subtrees if we know a root.
- So first use preorder or postorder traversal array to identify a root, and then use inorder traversal array to split
  an array into left and right.
  - For postorder traversal, need to make right subtree first, because in postorder, before root is right.
  - For preorder traversal, need to make left subtree first, because in preorder, after root is left.
- Make a hashmap where the key is the value in the preorder/postorder array and the value is the index in inorder array
  to make accessing inorder array easy.
- [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## Recursion

- `Top-down`
  - Set parameters to know the answer of the current node, and use the parameters and the answer of the current node to 
    solve the children of the current node.
- `Bottom-up`
  - Use the answer of the children of the current node, and calculate the answer of the current node.
- See the difference by pseudocode to find maximum value from the binary tree with the two approaches.

Top-down
```
return if root is null
if root is a leaf node:
    answer = max(answer, depth)
maximum_depth(root.left, depth + 1)
maximum_depth(root.right, depth + 1)
```

Bottom-up
```
return 0 if root is null
left_depth = maximum_depth(root.left)
right_depth = maximum_depth(root.right)
return max(left_depth, right_depth) + 1
```

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