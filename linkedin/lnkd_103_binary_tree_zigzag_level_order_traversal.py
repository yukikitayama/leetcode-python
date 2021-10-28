"""
- use queue
  - append nodes at the current level to the queue
  - BFS with flag
    - if flag is True, pop left from the queue,
    - if flag is False, pop right from the queue
"""


from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        # This is the queue to be added to answer list with zigzag order
        level_queue = collections.deque()

        # node_queue is a BFS queue
        node_queue = collections.deque([root, None])
        is_order_left = True

        # Traverse of each node is lever order left to right traversal
        # But when popping node from the queue, we make a temporary list
        # which holds nodes in zigzag order
        while node_queue:
            curr_node = node_queue.popleft()

            # print(f'curr_node: {curr_node}')
            # if curr_node:
            #     print(f'  curr_node.val: {curr_node.val}, is_order_left: {is_order_left}')

            if curr_node:
                # Visit nodes from left to right, same order maintained in level_queue
                if is_order_left:
                    level_queue.append(curr_node.val)
                # If is_order_left is False, keep the reverse order in level_queue
                else:
                    level_queue.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)

            # If current level finishes, node_queue pops None
            else:
                ans.append(list(level_queue))

                # Next level nodes are already in node_queue, so append None
                # to indicate the end of the next level
                # Need this if because only when there are next levelt nodes and add None can stop while loop
                # Without this if, while loop continues endlessly
                if node_queue:
                    node_queue.append(None)

                # It goes to the next level, so update level_queue and flag
                # Reset level queue
                level_queue = collections.deque()
                # Reverse the level direction
                is_order_left = not is_order_left

        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root = TreeNode(1)

print(Solution().zigzagLevelOrder(root))

