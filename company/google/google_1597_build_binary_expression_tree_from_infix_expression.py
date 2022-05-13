import collections


class Node:
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expTree(self, s: str) -> 'Node':
        # List of operands and operators
        tokens = collections.deque(list(s))

        # print(f'tokens: {tokens}')

        return self.parse_expression(tokens)

    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)

        while len(tokens) > 0 and tokens[0] in ['+', '-']:

            op = tokens.popleft()

            # rhs is Node
            rhs = self.parse_term(tokens)

            # print(f'  expression, left: {lhs.val}, op: {op}, right: {rhs.val}')

            lhs = Node(val=op, left=lhs, right=rhs)

        return lhs

    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)

        while len(tokens) > 0 and tokens[0] in ['*', '/']:

            op = tokens.popleft()

            # rhs is Node
            rhs = self.parse_factor(tokens)

            # print(f'    term, left: {lhs.val}, op: {op}, right: {rhs.val}')

            lhs = Node(val=op, left=lhs, right=rhs)

        # print(f'    exit term')

        return lhs

    def parse_factor(self, tokens) -> 'Node':
        if tokens[0] == '(':
            # Remove '('
            tokens.popleft()

            node = self.parse_expression(tokens)

            # Remove ')'
            tokens.popleft()

            # print(f'      factor if, node: {node.val}')

            return node

        # If single operand
        else:
            token = tokens.popleft()

            # print(f'      factor else, node: {token}')

            return Node(val=token)


if __name__ == '__main__':
    s = '3*4-2*5'
    ans = Solution().expTree(s)
    print(ans.val)
    print(ans.left.val, ans.right.val)
    print(ans.left.left.val, ans.left.right.val, ans.right.left.val, ans.right.right.val)
