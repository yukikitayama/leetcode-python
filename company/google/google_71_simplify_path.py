class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # print(f'path.split("/"): {path.split("/")}')

        for p in path.split('/'):

            if p == '..':
                if stack:
                    stack.pop()

            # Do nothing if current p is . or empty string
            elif p == '.' or not p:
                continue

            else:
                stack.append(p)

        # Leading '/' because canonical path needs to start with a single slash
        ans = '/' + '/'.join(stack)
        return ans


if __name__ == '__main__':
    path = "/home/"
    path = "/../"
    path = "/home//foo/"
    print(Solution().simplifyPath(path))
