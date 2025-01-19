from typing import List
import collections


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        counter = collections.Counter()
        ans = []
        balance = 0

        for i in range(len(A)):

            counter[A[i]] += 1
            if counter[A[i]] == 2:
                balance += 1

            counter[B[i]] += 1
            if counter[B[i]] == 2:
                balance += 1

            ans.append(balance)

        return ans

    def findThePrefixCommonArray1(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        set_a = set()
        set_b = set()

        for i in range(len(A)):

            set_a.add(A[i])
            set_b.add(B[i])
            ans.append(len(set_a.intersection(set_b)))

        return ans