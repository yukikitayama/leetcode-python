"""
Result
- Start: 7:04
- End: 7:28
- Solved: 0
- Saw solution: 1

Idea
- Union find?
- If two sets of email list have intersection, merge
  - Convert list of email strings to set
- If no intersection
  -
- Hashmap
  - Key: Name
  - Value: List of sets
"""


from typing import List
import collections
import pprint


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_to_set_list = collections.defaultdict(list)

        for account in accounts:
            name = account[0]
            emails = account[1:]

            if name not in name_to_set_list:
                name_to_set_list[name].append(set(emails))

            else:
                for i, set_list in enumerate(name_to_set_list[name]):

                    # print(f'i: {i}, set_list: {set_list}')

                    if set_list.intersection(set(emails)):
                        name_to_set_list[name][i] = set_list.union(set(emails))
                    else:
                        name_to_set_list[name].append(set(emails))

        # pprint.pprint(name_to_set_list)

        ans = []

        for name, set_list in name_to_set_list.items():
            # print(f'name: {name}, set_list: {set_list}')
            for emails in set_list:
                ans.append([name] + sorted(list(emails)))

        return ans


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts = [
    ["David","David0@m.co","David1@m.co"],
    ["David","David3@m.co","David4@m.co"],
    ["David","David4@m.co","David5@m.co"],
    ["David","David2@m.co","David3@m.co"],
    ["David","David1@m.co","David2@m.co"]
]
print(Solution().accountsMerge(accounts))




