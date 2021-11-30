"""
Idea
- DFS
- Email represents node,
- Edge represents two emails belong to the same person
- One account is one connected component
- Add an edge between two connected component
  if two accounts have an email in common
"""


from typing import List
import collections
import pprint


class Solution:
    def __init__(self):
        self.adjacent = collections.defaultdict(list)
        self.visited = set()

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_list_size = len(accounts)

        for account in accounts:
            account_size = len(account)
            account_first_email = account[1]

            # Make adjacency list
            # Add edge between first email and all other emails
            for i in range(2, account_size):
                account_email = account[i]
                self.adjacent[account_first_email].append(account_email)
                self.adjacent[account_email].append(account_first_email)

        # pprint.pprint(self.adjacent)

        ans = []

        for account in accounts:
            account_name = account[0]
            account_first_email = account[1]

            if account_first_email not in self.visited:
                merged_account = [account_name]

                self.dfs(merged_account, account_first_email)

                merged_account[1:len(merged_account)] = sorted(merged_account[1:len(merged_account)])

                ans.append(merged_account)

        return ans

    def dfs(self, merged_account, email):
        self.visited.add(email)
        merged_account.append(email)

        if email not in self.adjacent:
            return

        for neighbor in self.adjacent[email]:
            if neighbor not in self.visited:
                self.dfs(merged_account, neighbor)


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# accounts = [
#     ["David","David0@m.co","David1@m.co"],
#     ["David","David3@m.co","David4@m.co"],
#     ["David","David4@m.co","David5@m.co"],
#     ["David","David2@m.co","David3@m.co"],
#     ["David","David1@m.co","David2@m.co"]
# ]
print(Solution().accountsMerge(accounts))




