"""
bac
  abcabc

hashmap
  "a" -> "b",
  "b" -> "c",
  "c" -> "a"

should_see = "a"
Iterate from left to right
  should_see = "a"
    if see "b",
      increment ans
      should_see = "c"
    if see "a"
      should_see = "b"
  should_see = "c"
    if see "a"
      increment ans
      should_see = "b"
  should_see = "b"
    if see "c"
      increment ans
      should_see = "a"
    if see "a"
      increment ans by 2
      should_see = "b"
    if see "b"
      should_see = "c"

Edge case
  if word doesn't end with c
    end with a
      increment by 2
    end with b
      increment by 1

-1 % 2
"""


class Solution:
    def addMinimum(self, word: str) -> int:
        conversion = {
            "a": "b",
            "b": "c",
            "c": "a"
        }

        ans = 0

        should_see = "a"

        for i in range(len(word)):

            if word[i] == should_see:
                should_see = conversion[word[i]]
                continue

            diff = (ord(word[i]) - ord(should_see)) % 3
            ans += diff
            should_see = conversion[word[i]]

        # Post process
        if word[-1] == "a":
            ans += 2
        elif word[-1] == "b":
            ans += 1

        return ans

    def addMinimum1(self, word: str) -> int:

        conversion = {
            "a": "b",
            "b": "c",
            "c": "a"
        }

        ans = 0

        should_see = "a"

        for i in range(len(word)):

            if word[i] == should_see:
                should_see = conversion[word[i]]
                continue

            if should_see == "a":
                if word[i] == "b":
                    ans += 1
                elif word[i] == "c":
                    ans += 2

            elif should_see == "b":
                if word[i] == "c":
                    ans += 1
                elif word[i] == "a":
                    ans += 2

            elif should_see == "c":
                if word[i] == "a":
                    ans += 1
                elif word[i] == "b":
                    ans += 2

            should_see = conversion[word[i]]

        # Pos process
        if word[-1] == "a":
            ans += 2
        elif word[-1] == "b":
            ans += 1

        return ans
