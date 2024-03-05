# Tree

- An undirected graph in which any two vertices are connected by exactly one path
- Any connected graph without cycles is a tree.

## Valid tree

A given graph is a valid tree is it's **fully connected** and there is **no cycle**.

For the graph to be a valid tree, it must have exactly `n - 1` edges. Any less is not fully connected. Any more contains cycles.

If a graph is fully connected AND contains exactly `n - 1` edges, it's a valid tree without a cycle.

https://leetcode.com/problems/graph-valid-tree/description/

## Binary Tree

- Recursion template. Key is to implement `if node is None` for how to end the recursion.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(node, other_information):
    if node is None:
        return 'Things like 0 or None'
    else:
        'Do something relates to helpe(node.left) and helper(node.right)'

def answer_to_problem(root):
    return helper(root, 'other_information')
```

- Inorder traversal
  - `Left -> Root -> Right`
- Preorder traversal
  - `Root -> Left -> Right`
- Postorder traversal
  - `Left -> Right -> Root`
- [All DFS traversals (preorder, inorder, postorder) in Python in 1 line](https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line)

### Morris Preorder Traversal

- Morris preorder traversal is constant space for DFS preorder traversal in binary tree, while recusrive and iterative
  DFS use `O(H)` space where `H` is the height of the binary tree.
  - Recursion uses recursion stack for `O(H)`
  - Iteration uses queue for `O(H)`

#### Problem

- [1022. Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)

## Decision Tree

- A special form of binary tree used in classification and regression.
- Decision node
  - Non-leaf node.
  - Each decision node contains a condition as a branching rule.
    - Less-then-or-equal comparison
    - Membership of category
- Each leaf node contains a label assigned to objects which fall into this leaf.
- Stopping condition
  - All the data fall into a node belong to the same category.
  - The tree reaches the predefined maximum depth.
  - The number of examples fall into a node is less than the predefined minimum number of data in a node.


## Binary Search Tree (BST)

- Inorder traversal of a binary search tree gives nodes in the ascending order.
- Inorder is `left -> root -> right`.

### Example

- Problems to solve by using BST properties
  - [669. Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)
