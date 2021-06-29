import collections


class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        # (digit, depth)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()

            if node == target:
                return depth

            if node in dead:
                continue

            for neighbor in self.neighbors(node):
                print(f'Node: {node}, neighbors: {neighbor}')
                if neighbor not in seen:
                    seen.add(neighbor)
                    # Increment depth
                    queue.append((neighbor, depth + 1))

        return -1

    def neighbors(self, node):
        for i in range(4):
            x = int(node[i])
            for d in (-1, 1):
                # below modulo operator
                y = (x + d) % 10

                yield node[:i] + str(y) + node[i + 1:]


deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
sol = Solution()
answer = sol.openLock(deadends, target)
print(f'Answer: {answer}')