"""
DFS
  create graph
    first to others
    others to first
    if one account only has one account,
      skip
      not part of graph
"""

from typing import List
import collections


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = collections.defaultdict(list)
        for account in accounts:
            name = account[0]
            emails = account[1:]

            if len(emails) > 1:
                for i in range(1, len(emails)):
                    graph[emails[0]].append(emails[i])
                    graph[emails[i]].append(emails[0])

        print(graph)

        visited = set()

        def dfs(list_, email):
            visited.add(email)
            list_.append(email)

            if email not in graph:
                return

            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(list_, neighbor)

        ans = []

        for account in accounts:

            name = account[0]
            first_email = account[1]

            if first_email not in visited:
                curr = [name]
                dfs(curr, first_email)

                emails = curr[1:]
                emails.sort()
                curr[1:] = emails

                ans.append(curr[:])

        return ans
