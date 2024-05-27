class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        p_to_s = {}
        word_set = set()

        def backtracking(p_i, s_i):

            # Terminate
            if p_i == len(pattern):
                # Check if also exhausted s
                return s_i == len(s)

            symbol = pattern[p_i]

            if symbol in p_to_s:
                word = p_to_s[symbol]

                if s[s_i:s_i + len(word)] != word:
                    return False

                return backtracking(p_i + 1, s_i + len(word))

            # New word
            for end in range(s_i + 1, len(s) + 1):

                new_word = s[s_i:end]

                # bijection constraint
                # {a: xy}, new_word: xy, but we cannot reverse map this xy to different key
                # Before this for-loop, we already check current key doesn't exist in map
                if new_word in word_set:
                    continue

                p_to_s[symbol] = new_word
                word_set.add(new_word)

                if backtracking(p_i + 1, s_i + len(new_word)):
                    return True

                # Backtrack
                del p_to_s[symbol]
                word_set.remove(new_word)

        return backtracking(0, 0)

    def wordPatternMatch1(self, pattern: str, s: str) -> bool:

        def backtracking(start, curr_map, pattern_i):

            if start == len(s):
                print(curr_map)
                return

            # Fail
            if pattern_i == len(pattern) and start < len(s):
                return

            for end in range(start, len(s)):

                curr_str = s[start:end + 1]
                pattern_str = pattern[pattern_i]

                if pattern_str not in curr_map:
                    curr_map[pattern_str] = curr_str
                elif pattern_str in curr_map and curr_map[pattern_str] != curr_str:
                    return

                print(curr_map)

                backtracking(end + 1, curr_map, pattern_i + 1)

                # Backtrack
                del curr_map[pattern_str]

        backtracking(0, {}, 0)

        return False
