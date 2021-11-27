"""
Idea
- Use stack because tags are nested. Recent start tag is at the top of stack
  and the incoming end tag needs to match with last in start tag, not first in start tag

"""


class Solution:

    def __init__(self):
        self.stack = []
        self.contains_tag = False

    def isValid(self, code: str) -> bool:

        # print(f'len(code): {len(code)}')

        if code[0] != '<' or code[len(code) - 1] != '>':
            return False

        # for i in range(len(code)):
        i = 0
        while i < len(code):

            # print(f'  i: {i}, code[i]: {code[i]}')

            ending = False

            # In helper function, contains_tag changed to True and something pushed to stack
            # So if stack is empty but if contains_tag still show there's something it's invalid
            if not self.stack and self.contains_tag:
                return False

            if code[i] == '<':
                # CDATA needs to be between start tag and end tag,
                # which means there's something in stack
                if self.stack and code[i + 1] == '!':
                    # Find the index of closing of CDATA in the i + 1 following string
                    # find() returns -1 if not found, but index() throws error if not found
                    close_index = code.find(']]>', i + 1)

                    # i + 2 because the first 2 characters are '<' and 'i' for CDATA
                    if close_index < 0 or not self.is_valid_cdata(code[i + 2:close_index]):
                        # print(f'here, close_index: {close_index}, is_valid_cdata: {self.is_valid_cdata(code[i + 2:close_index])}')
                        return False

                else:
                    if code[i + 1] == '/':
                        i += 1
                        ending = True

                    close_index = code.find('>', i + 1)
                    if close_index < 0 or not self.is_valid_tag_name(code[i + 1:close_index], ending):
                        # print(f'here, close_index: {close_index}, is_valid_tag_name: {self.is_valid_tag_name(code[i + 1:close_index], ending)}')
                        return False

                # Move i to the close index because we wanna skip things inside of the tag between < and >
                i = close_index

            i += 1

        return not self.stack and self.contains_tag

    def is_valid_tag_name(self, s: str, ending: bool) -> bool:

        # print(f'    is_valid_tag_name, s: {s}, ending: {ending}')

        if len(s) < 1 or len(s) > 9:
            return False

        for i in range(len(s)):
            if not s[i].isupper():
                return False

        if ending:
            # If there's something in stack and stack top is equal to s
            if self.stack and self.stack[-1] == s:
                # The start tag in stack becomes a pair with the current s end tag,
                # so remove it from stack
                self.stack.pop()
            # If the current s is end tag, and stack is empty or stack top is not equal, invalid
            else:
                return False
        else:
            self.contains_tag = True
            self.stack.append(s)

        return True

    def is_valid_cdata(self, s):
        return s.find('[CDATA[') == 0


code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
# True
code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
# True
code = "<A>  <B> </A>   </B>"
# False
code = "<DIV>  div tag is not closed  <DIV>"
# False
print(Solution().isValid(code))


