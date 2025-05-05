"""
Stack
  digits stack
    with digit, keep extracting until [
  character stack
    start extracting with [
    keep extracting until next is not character (], digit)
  when seeing ],
    pop digit stack until empty
     and character stack, multiply
    push back to character
Return character stack by joining
eg1
  "3[a]2[bc]"
  ds: [3]
  cs: [a]
  ], 3, a, aaa, cs: [], cs: [aaa]
    edge
  ds: [2]
  cs: [aaa, bc]
  ], 2, bc, bcbc, cs: [aaabcbc]
  retrun aaaabcbc
eg2
  "3[a2[c]]"
  ds: [3]
  cs: [a]
  ds: [3, 2]
  cs: [a, c]
  see ]
  2, c, cc, [acc] (concat with previous)

  ], acc, 3, accaccacc

https://leetcode.com/problems/decode-string/description/
"""


class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        curr_string = ""
        curr_num = 0

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)

            elif c == "[":
                count_stack.append(curr_num)
                string_stack.append(curr_string)
                curr_string = ""
                curr_num = 0

            elif c == "]":
                # print(count_stack, string_stack, curr_string)
                popped_string = string_stack.pop()
                popped_count = count_stack.pop()
                for _ in range(popped_count):
                    popped_string = popped_string + curr_string
                curr_string = popped_string

            else:
                curr_string += c

        return curr_string