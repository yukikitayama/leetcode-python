"""
- Siblings means the nodes that share the same direct parent at the same level
  - Use right pointer to connect current node to the next node
- Connect head of siblings to parent
- Left: Parent to head of siblings
- Right: Links between nodes in siblings
- Traverse level by level for siblings
"""


from typing import Optional
import collections


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return

        root_tree_node = TreeNode(root.val)
        # Queue: [(TreeNode, Node), ...]
        queue = collections.deque([(root_tree_node, root)])

        while queue:

            parent_tree_node, curr_node = queue.popleft()

            # Reset head and prev in each parent
            head_tree_node = None
            prev_tree_node = None

            if curr_node.children:
                for child in curr_node.children:

                    child_tree_node = TreeNode(child.val)

                    if not head_tree_node:
                        head_tree_node = child_tree_node
                    if prev_tree_node:
                        prev_tree_node.right = child_tree_node

                    prev_tree_node = child_tree_node

                    queue.append((child_tree_node, child))

                parent_tree_node.left = head_tree_node

        return root_tree_node

    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return

        # Node(val, children)
        root_node = Node(data.val, [])

        # Queue: [(Node, TreeNode)]
        queue = collections.deque([(root_node, data)])

        while queue:

            parent_node, current_tree_node = queue.popleft()

            # Reset each parent tree node
            child_tree_node = current_tree_node.left

            while child_tree_node:

                child_node = Node(child_tree_node.val, [])
                parent_node.children.append(child_node)

                queue.append((child_node, child_tree_node))

                child_tree_node = child_tree_node.right

        return root_node


if __name__ == '__main__':
    root = Node(1)
    root.children = [Node(2), Node(3), Node(4)]
    root.children[0].children = [Node(5), Node(6), Node(7)]
    root.children[2].children = [Node(8), Node(9), Node(10)]
    codec = Codec()
    encoded = codec.encode(root)
    # while encoded:
    #     print(encoded.val)
    #     encoded = encoded.left
    decoded = codec.decode(encoded)
    print(decoded.val)
    for child in decoded.children:
        print(f'  child: {child.val}')
