"""
screen given ip to v4 or v6 by . or :
if v4
  apply v4 rule
    while to iterate each character
      if curr char is 0, check if
        it's the end
        next is .
        this 0 is after some number
if v6
  apply v6 rule

Ans
  divide and conquer

"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def check_v4(s):
            num_strs = s.split(".")
            for num_str in num_strs:
                if len(num_str) == 0:
                    return "Neither"
                if num_str.isdigit() and int(num_str) > 255:
                    return "Neither"
                if len(num_str) > 1 and num_str[0] == "0":
                    return "Neither"
                if not num_str.isdigit():
                    return "Neither"
            return "IPv4"

        def check_v6(s):
            items = s.split(":")
            valid_chars = "0123456789abcdefABCDEF"
            for x in items:
                if len(x) == 0:
                    return "Neither"
                if len(x) > 4:
                    return "Neither"
                if not all(c in valid_chars for c in x):
                    return "Neither"
            return "IPv6"

        if queryIP.count(".") == 3:
            return check_v4(queryIP)
        elif queryIP.count(":") == 7:
            return check_v6(queryIP)
        else:
            return "Neither"
