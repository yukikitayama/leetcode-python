"""
Hashmap
  k: value
  v: treenode
If parent not in hashmap
  Create a new node and save it to hashmap
else
  update their children
if child not in hashmap
  Create a new node and save it to hashmap
else
  ___
Hashset
  add child
Return treenode value from the hashmap whose key doesn't exist in hashset
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children_set = set()
        value_to_node = {}

        # Iterate descriptions and update hashmap
        for parent, child, is_left in descriptions:

            children_set.add(child)

            if parent not in value_to_node:
                parent_node = TreeNode(parent)
                value_to_node[parent] = parent_node

            if child not in value_to_node:
                child_node = TreeNode(child)
                value_to_node[child] = child_node

            if is_left == 1:
                value_to_node[parent].left = value_to_node[child]
            else:
                value_to_node[parent].right = value_to_node[child]

        for k, v in value_to_node.items():
            if k not in children_set:
                return v

    def createBinaryTree1(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children_set = set()
        value_to_node = {}

        # Iterate descriptions and update hashmap
        for parent, child, is_left in descriptions:

            children_set.add(child)

            if parent not in value_to_node and child not in value_to_node:
                parent_node = TreeNode(parent)
                value_to_node[parent] = parent_node

                child_node = TreeNode(child)
                value_to_node[child] = child_node

            elif parent in value_to_node and child not in value_to_node:
                child_node = TreeNode(child)
                value_to_node[child] = child_node

            elif parent not in value_to_node and child in value_to_node:
                parent_node = TreeNode(parent)
                value_to_node[parent] = parent_node

            elif parent in value_to_node and child in value_to_node:
                pass

            if is_left == 1:
                value_to_node[parent].left = value_to_node[child]
            else:
                value_to_node[parent].right = value_to_node[child]

        for k, v in value_to_node.items():
            if k not in children_set:
                return v