class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def match(text, pattern):

            # If pattern is '', meaning the end of characters,
            # text should also be '', to return True
            if not pattern:
                return not text

            # Only text: '' returns False by bool(text)
            first_match = bool(text) and pattern[0] in {text[0], '.'}

            if len(pattern) >= 2 and pattern[1] == '*':

                # Ignore or (Delete)
                # Ignore means don't use *
                # Delete means use * and go to the next character in text
                return match(text, pattern[2:]) or (first_match and match(text[1:], pattern))

            # Recursively check the next character
            else:
                return first_match and match(text[1:], pattern[1:])

        return match(s, p)


if __name__ == '__main__':
    s = 'aa'
    p = 'a.'
    # p = 'a'
    print(Solution().isMatch(s, p))
