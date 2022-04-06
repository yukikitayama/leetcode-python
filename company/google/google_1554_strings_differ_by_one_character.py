from typing import List


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n = len(dict)
        m = len(dict[0])

        for j in range(m):
            seen = set()
            for i in range(n):
                new_w = dict[i][:j] + '*' + dict[i][j + 1:]
                if new_w in seen:
                    return True
                seen.add(new_w)

        return False


if __name__ == '__main__':
    dict = ["abcd", "acbd", "aacd"]
    print(Solution().differByOne(dict))
