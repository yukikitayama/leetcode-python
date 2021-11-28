class Solution:
    def levelOrder(self, root):
        # Initialize answer
        answer = []

        # Input TreeNode root could be None (Null), if not None
        if not root:
            return answer

        level = 0
        queue = [root]
        while queue:
            # Initialize list of each level
            answer.append([])

            curr_num_nodes = len(queue)

            for i in range(curr_num_nodes):
                node = queue.pop(0)

                answer[level].append(node.val)

                # Add nodes at the next level to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Update level and go down
            level += 1

        return answer


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node0 = TreeNode(val=3)
node1 = TreeNode(val=9)
node2 = TreeNode(val=20)
node3 = TreeNode(val=15)
node4 = TreeNode(val=7)

node0.left = node1
node0.right = node2
node2.left = node3
node2.right = node4

sol = Solution()
answer = sol.levelOrder(root=node0)
print(f'Answer: {answer}')
