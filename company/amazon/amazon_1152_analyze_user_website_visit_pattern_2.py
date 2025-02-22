import itertools
import collections
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_to_websites = collections.defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website)):
            user_to_websites[u].append(w)

        # print(user_to_websites)

        pattern_to_user_count = collections.Counter()
        for user, websites in user_to_websites.items():

            counter = collections.Counter()
            for combination in set(itertools.combinations(websites, 3)):
                counter[combination] += 1

            pattern_to_user_count += counter

        # print(pattern_to_user_count)

        ans = []
        max_count = max(pattern_to_user_count.values())
        for pattern, user_count in pattern_to_user_count.items():
            if user_count == max_count:
                ans.append(pattern)
        ans.sort()
        return ans[0]