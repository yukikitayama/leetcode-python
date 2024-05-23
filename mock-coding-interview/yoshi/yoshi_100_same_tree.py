# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # If both missing
        # Edge case: this also checks missing root case
        if not p and not q:
            return True

        # Because already check both missing, below means one of them could be missing
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        # We guarantee to have p and q, because at the top, already checked whether p and q are not None
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(curr_p, curr_q):
            nonlocal ans

            if curr_p and curr_q:

                if curr_p.val != curr_q.val:
                    ans = False
                    return

                if curr_p.left and curr_q.left:
                    dfs(curr_p.left, curr_q.left)
                elif curr_p.left and not curr_q.left:
                    ans = False
                    return
                elif not curr_p.left and curr_q.left:
                    ans = False
                    return

                if curr_p.right and curr_q.right:
                    dfs(curr_p.right, curr_q.right)
                elif curr_p.right and not curr_q.right:
                    ans = False
                    return
                elif not curr_p.right and curr_q.right:
                    ans = False
                    return

            elif not curr_p and not curr_q:
                return
            else:
                ans = False
                return

        dfs(p, q)

        return ans
