"""
conversion
  . -> current holder
  .. -> parent holder
  // -> /
  ending / -> ""

Use stack to collect path element
  stack only contains directory and file names, no /
split path by delimiter /
while iterate given path
  while loop to create current element (directory or file)
    / or // indicates the end of current
  .. is stack top

eg1
  [/, home]
eg2
  [/]
eg3
  [/, home, foo]
/../../../test
  [/, test]

t: O(N)
s: O(N)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:

        # "/a//b///c/".split("/"): ["", a, "", b, "", "", c, ""]
        path_list = path.split("/")

        # print(path_list)

        stack = []

        for i in range(len(path_list)):

            curr = path_list[i]

            if curr not in ["", "."]:

                if curr == "..":
                    if stack:
                        popped = stack.pop()

                else:
                    stack.append(curr)

        # print(stack)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    path = "/home/"
    path = "/../"
    path = "/home//foo/"
    path = "/../../../test"
    path = "/a/./b/../../c/"