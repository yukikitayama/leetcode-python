class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for file_ in path.split("/"):

            if file_ == "..":
                if stack:
                    stack.pop()

            elif file_ == "." or file_ == "":
                continue

            else:
                stack.append(file_)

        return "/" + "/".join(stack)

    def simplifyPath1(self, path: str) -> str:
        stack = []

        i = 0

        while i < len(path):

            if path[i] == "/":
                i += 1

            else:
                curr = []
                while i < len(path) and path[i] != "/":
                    curr.append(path[i])
                    i += 1
                curr = "".join(curr)

                if curr == ".":
                    continue
                elif curr == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(curr)

        return "/" + "/".join(stack)
