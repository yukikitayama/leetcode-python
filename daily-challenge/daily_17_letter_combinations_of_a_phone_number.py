from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        ans = []

        def backtracking(path, index):

            # print(f'path: {path}, index: {index}')

            if index >= len(digits):
                ans.append(''.join(path))
                return

            digit = digits[index]
            letters = digit_to_letters[digit]

            for letter in letters:

                path.append(letter)

                backtracking(path, index + 1)

                # Backtrack
                path.pop()

        backtracking([], 0)

        return ans


if __name__ == '__main__':
    digits = '23'
    digits = ''
    print(Solution().letterCombinations(digits))
