"""
- Two pointers
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            # j == 0: first type is different
            # !=: not long pressed
            elif j == 0 or typed[j] != typed[j - 1]:
                return False

        return i == len(name)


if __name__ == '__main__':
    name = 'alex'
    # typed = 'aaleex'
    typed = 'aaleexx'
    # name = 'saeed'
    # typed = 'ssaaedd'
    # name = "vtkgn"
    # typed = "vttkgnn"
    # true
    name = "alex"
    typed = "aaleelx"
    print(Solution().isLongPressedName(name, typed))
