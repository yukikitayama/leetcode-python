import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()

        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):

            if c not in seen:

                # It can delete the characters store in stack
                # if the current character is smaller than the previous character
                # and if the previous character will appear later
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    popped_c = stack.pop()
                    # By discarding the item from the set, we can again visit the discard character later
                    # discard() doesn't raise an error while remove() does
                    seen.discard(popped_c)

                seen.add(c)
                stack.append(c)

        return ''.join(stack)


"""
- Space is O(1) because seen set and stack are bounded by the number of characters 26, 
  because the contents are unique characters
"""


class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:

        c = collections.Counter(s)

        # print(f'c: {c}, s: {s}')

        # Index of the leftmost letter
        pos = 0

        for i in range(len(s)):

            # Update smallest character index
            if s[i] < s[pos]:
                pos = i

            c[s[i]] -= 1

            # print(f'  i: {i}, pos: {pos}, c: {c}')

            if c[s[i]] == 0:
                break

        # Answer is the leftmost character plus the recursion on the remainder string
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], '')) if s else ''


if __name__ == '__main__':
    s = 'bcabc'
    s = 'abc'
    s = 'abca'
    s = 'bab'
    print(Solution().removeDuplicateLetters(s))
