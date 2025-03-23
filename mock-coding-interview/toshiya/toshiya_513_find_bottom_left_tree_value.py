from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = None
        queue = collections.deque([root])
        print(queue)
        print()
        while queue:
            for i in range(len(queue)):

                # e.g. 1
                # 1: [2] -> [] -> [1, 3]
                # 2: [1, 3] -> [] -> []
                # e.g. 2
                # 1: [1] -> [] -> [2, 3]
                # 2: [2, 3] -> [] -> [4, 5, 6]
                # 3: [4, 5, 5] -> [] -> [7]
                # 4: [7] -> [] -> []
                curr = queue.popleft()
                print(curr)
                print()

                if i == 0:
                    ans = curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return ans


"""
array = [1, 2, 3]
var = array.pop()
var: 3
array: [1, 2]
array.popleft(): no
array = array[1:]
T: O(N)
array: [1, 2, 3, ... 100]
array[1:]
array: [_, 2, 3, ... 100]
array: [<-2, <-3, ..., <-100]
deque: looks array, linked list
queue: [1] <- [2] <- [3]
queue.popleft()
queue:        [2] <- [3]
"""