from typing import List
import collections
import itertools


class Solution:

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_to_website = collections.defaultdict(list)

        # Sort to have correct order of visiting websites
        for u, t, w in sorted(zip(username, timestamp, website)):
            user_to_website[u].append(w)

        # print(user_to_website)

        pattern_to_num_user = collections.Counter()

        for user, websites in user_to_website.items():

            counter = collections.Counter()
            # set() because we wanna have distinct pattern for each user
            # If one user has ["a", "a", "a", "a"], it gives 4 ["a", "a", "a"]
            # to count the number of users, distinct pattern for each user is fine.
            for combination in set(itertools.combinations(websites, 3)):
                counter[combination] += 1

            pattern_to_num_user += counter

        # print(pattern_to_num_user)

        patterns = []

        # Find patterns with largest score
        max_num = max(pattern_to_num_user.values())
        for k, v in pattern_to_num_user.items():
            if v == max_num:
                patterns.append(list(k))

        # Get lexicographically smallest pattern
        patterns.sort()
        return patterns[0]
