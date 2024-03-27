"""
0: -5
1: 10
2: -5
  1 gives $5 to 0
  1 givea $5 to 2

0: -4
1: 4
2: 0

Compute balance of each person
Subtract negative amounts from positive amounts
min heap and max heap
"""

from typing import List
import collections
import heapq


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        person_to_balance = collections.defaultdict(int)

        for from_, to, amount in transactions:
            person_to_balance[from_] -= amount
            person_to_balance[to] += amount

        balance_list = [balance for balance in person_to_balance.values() if balance]

        print(balance_list)

        n = len(balance_list)

        def backtracking(curr):

            # Skip transaction when balances are 0 (became 0 in the loop)
            while curr < n and balance_list[curr] == 0:
                curr += 1

            # No more transaction if we processed all
            if curr == n:
                return 0

            cost = float("inf")

            for next_ in range(curr + 1, n):

                # Find (pos, neg) or (neg, pos) pair
                if balance_list[next_] * balance_list[curr] < 0:
                    # Transfer current balance to next
                    # Actually don't make curr balance be 0, but behaving like it became 0
                    balance_list[next_] += balance_list[curr]

                    cost = min(cost, 1 + backtracking(curr + 1))

                    # Backtrack
                    balance_list[next_] -= balance_list[curr]

            return cost

        return backtracking(0)

    def minTransfers1(self, transactions: List[List[int]]) -> int:
        person_to_balance = collections.defaultdict(int)

        for from_, to, amount in transactions:
            person_to_balance[from_] -= amount
            person_to_balance[to] += amount

        print(person_to_balance)

        min_heap = []
        heapq.heapify(min_heap)
        max_heap = []
        heapq.heapify(max_heap)

        for balance in person_to_balance.values():

            if balance < 0:
                heapq.heappush(min_heap, balance)
            elif balance > 0:
                heapq.heappush(max_heap, -balance)

        print("min_heap (debts)", min_heap)
        print("max_heap (credits)", max_heap)

        ans = 0

        while min_heap:

            debt = heapq.heappop(min_heap)
            credit = heapq.heappop(max_heap)

            # Debt: -2, credit: -1
            if abs(debt) > abs(credit):
                debt -= credit
                heapq.heappush(min_heap, debt)

            else:
                credit -= debt
                if credit != 0:
                    heapq.heappush(max_heap, credit)

            ans += 1

        return ans
