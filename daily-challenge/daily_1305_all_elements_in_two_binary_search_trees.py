"""
- Inorder traversal 2 times, because it's binary search tree
- Iterate two sorted list to make one sorted list
- Time is O(N + M)
- Space is O(N + M)
"""


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class OnePassSolution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, ans = [], [], []

        while root1 or root2 or stack1 or stack2:
            while root1:
                # root is at the bottom of the stack
                # next append left child, but popped first
                # Later update root1 with right child, so up right child on top of root
                stack1.append(root1)
                root1 = root1.left

            while root2:
                stack2.append(root2)
                root2 = root2.left

            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                ans.append(root1.val)
                root1 = root1.right

            else:
                root2 = stack2.pop()
                ans.append(root2.val)
                root2 = root2.right

        return ans


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        inorder1 = inorder(root1)
        inorder2 = inorder(root2)

        # print(f'inorder1: {inorder1}')
        # print(f'inorder2: {inorder2}')

        ans = []
        i = 0
        j = 0
        while i < len(inorder1) and j < len(inorder2):
            if inorder1[i] < inorder2[j]:
                ans.append(inorder1[i])
                i += 1
            else:
                ans.append(inorder2[j])
                j += 1

        # print(f'i: {i}, j: {j}')

        if i != len(inorder1):
            ans.extend(inorder1[i:])
        elif j != len(inorder2):
            ans.extend(inorder2[j:])

        return ans


if __name__ == '__main__':
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)
    print(Solution().getAllElements(root1, root2))
