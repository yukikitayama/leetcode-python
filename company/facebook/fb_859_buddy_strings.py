class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        # If lengths are different, swapping won't work
        if len(s) != len(goal):
            return False

        # If initially s and goal are the same,
        # there must be duplicate characters
        # so you can swap them but still the same string
        # if there are not duplicate characters, but you still need to swap
        # , which will s and goal be different
        if s == goal:
            seen = set()

            for char in s:

                if char in seen:
                    return True

                seen.add(char)

            return False

        pairs = []
        for a, b in zip(s, goal):

            # Count how many there are different characters possibly need to be swapped
            if a != b:
                pairs.append((a, b))

            # If you have more than or equal to 3 pairs
            # You need to swap more than 1 time, so it's false in this problem
            # because we can only swap once
            if len(pairs) >= 3:
                return False

        print(f'pairs: {pairs}')
        print(f'pairs[0]: {pairs[0]}')
        print(f'pairs[1][::-1]: {pairs[1][::-1]}')

        # Different pair number need to be 2 for 1 swap to make them equal
        # and pairs[1][::-1] actually swap it to test whether it has the same expression
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


if __name__ == '__main__':
    s = 'abc'
    goal = 'bdc'
    print(Solution().buddyStrings(s, goal))

