"""
start from counting consecutive t and f without thinking about k
answerKey: 'TTFF'
t: [1, 2, 0, 0]
f: [0, 0, 1, 2]

k: 2
t: [1, 2, 3, 4]
f: [1, 2, 3, 4]

answerKey: 'TFFT'
t: [1, 0, 0, 1]
f: [0, 1, 2, 0]

k: 1
t: [1, 2, 0, 1], [1, 0, 1, 2]
f: [1, 2, 3, 0], [0, 1, 2, 3]

answerKey: "TTFTTFTT"
t: [1, 2, 0, 1, 2, 0, 1, 2]
f: [0, 0, 1, 0, 0, 1, 0, 0]

use t


k: 1
t: [1, 2, 3, 4, 5, 0, 1, 2], [1, 2, 0, 1, 2, 3, 4, 5]
f: [0, 0, 1, 2]

count t and f in answerKey
use t or f which has larger number of characters

scan from left to right
- dp_t[i] represents the max number of consecutive T so far
dp_t: [1, 2, 0, 0]
i: 2, if k > 0, dp_t[2]: 3

- dp_f[i] represents the max number of consecutive F so far
"""


from collections import Counter


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: str) -> int:

        ans = 0

        # for start in range(len(answerKey)):
        #     if


answerKey = "TTFTTFTT"
k = 1
# answerKey = "TFFT"
# k = 1
# answerKey = "FFFTTFTTFT"
# k = 3
# answerKey = "TTFF"
# k = 1
print(Solution().maxConsecutiveAnswers(answerKey, k))
