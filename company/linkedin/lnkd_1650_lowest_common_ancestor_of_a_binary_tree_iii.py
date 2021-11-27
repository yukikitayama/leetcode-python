"""
- Lowest means, in binary tree, the deepest, the maximum depth,
  - Not about the val in Node
- https://en.wikipedia.org/wiki/Lowest_common_ancestor
- https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/932914/Java-in-6-lines
- https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/932499/Simple-Python-Solution-with-O(1)-space-complexity
- Apply Approach 3: Two Pointers in https://leetcode.com/problems/intersection-of-two-linked-lists/solution/

- p and q could have different distance to root
- but they share the root
- when p reaches root, start over from q
- when q reaches root, start over from p
- The steps that both p and q experience is the same
  - Let a be the steps from p to the lowest common node
  - Let b be the steps from q to the lowest common node
  - Let c be the steps from the lowest common node to root
  - p experiences, a -> c -> b
  - q experiences, b -> c -> a
  - So both steps are the same
  - After b of p experience, and after a of q experience,
    both p and q are at the lowest common node to meet up
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        curr_p, curr_q = p, q

        while curr_p != curr_q:
            curr_p = curr_p.parent if curr_p.parent else q
            curr_q = curr_q.parent if curr_q.parent else p

        # p and q are somewhere inside the binary tree,
        # so it's guaranteed for current p and q meet up somewhere
        return curr_p






