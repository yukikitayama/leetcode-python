class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # [(character, count), ...]
        stack = []

        for c in s:

            if stack and stack[-1][0] == c:
                # Count up because it sees the consequent same characters
                stack[-1][1] += 1

            else:
                # 1 because a new non-consequent character faced
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        print(f'stack: {stack}')

        return ''.join(character * count for character, count in stack)


if __name__ == '__main__':
    s = 'abb'
    k = 2
    # s = "abcd"
    # k = 2
    s = "deeedbbcccbdaa"
    k = 3
    # aa
    print(Solution().removeDuplicates(s, k))
