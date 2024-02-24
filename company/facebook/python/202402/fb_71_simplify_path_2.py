"""
/a/b/../c
  /a/b/c

/a/b/../../c
  /a/c

Clean slash
empty stack
split path by /
iterate file/directory
  if curr is ..,
    pop stack
  else
    append curr
Join stack by /
Add / at start
"""



class Solution:
    def simplifyPath(self, path: str) -> str:
        # /home//foo/ will be ["", home, "", foo, ""]
        file_directory = path.split("/")
        # print(file_directory)
        stack = []

        for i in range(len(file_directory)):

            curr = file_directory[i]

            if curr == "..":
                if stack:
                    stack.pop()
            elif curr == "":
                continue
            elif curr == ".":
                continue
            else:
                stack.append(curr)

        ans = "/" + "/".join(stack)
        return ans
