from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, buffer, block_comment_open = [], '', False

        for line in source:
            # Pointer in each line
            i = 0
            while i < len(line):

                char = line[i]

                # Check // Line comment
                # Check length before line[i + 1] to avoid index out of bound
                if char == '/' and (i + 1) < len(line) and line[i + 1] == '/' and not block_comment_open:
                    # To omit anything after //, move the pointer to the end of the line
                    i = len(line)

                # Check /* start of block comment
                elif char == '/' and (i + 1) < len(line) and line[i + 1] == '*' and not block_comment_open:
                    # Signal we are in the block comment in the following iteration
                    block_comment_open = True
                    i += 1

                # Check */ end of block comment
                elif char == '*' and (i + 1) < len(line) and line[i + 1] == '/' and block_comment_open:
                    # Signal we finished the block comment
                    block_comment_open = False
                    i += 1

                # Normal character that we need to track, which needs to be out of block comment
                elif not block_comment_open:
                    buffer += char

                i += 1

            # If we finished the current line, and buffer is not empty (if '' is False)
            # and currently not in the block comment
            if buffer and not block_comment_open:
                res.append(buffer)

                # Reset buffer for the next line
                buffer = ''

        return res


"""
Time complexity
Let m be the length of source, and n be the average length of each line
O(mn) because it iterates all the characters

Space complexity
O(max(length of each line)) for buffer
"""


source = [
    "/*Test program */",
    "int main()",
    "{ ",
    "  // variable declaration ",
    "int a, b, c;",
    "/* This is a test",
    "   multiline  ",
    "   comment for ",
    "   testing */",
    "a = b + c;",
    "}"
]
answer = Solution().removeComments(source)
for line in answer:
    print(line)
