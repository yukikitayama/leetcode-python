"""
hashmap
  k: char in key
  v: a to z
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        k_to_c = {}
        j = 0
        for i in range(len(key)):
            if key[i].isalpha() and key[i] not in k_to_c:
                k_to_c[key[i]] = chr(ord('a') + j)
                j += 1

        ans = []
        for k in message:
            if k == " ":
                ans.append(k)
            else:
                ans.append(k_to_c[k])

        return "".join(ans)
