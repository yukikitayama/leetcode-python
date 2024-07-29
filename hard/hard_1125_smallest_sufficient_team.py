"""
n: length of people array
m: length of skill array
bitmask for skill
  2 ** (m - 1). -1 becuase 0th position can be used
    e.g. m: 3, 2**3 = 8, bin(8): 1000, bin(8 - 1): 0111, three 1 bits
  skillsMask
bitmask of skill for each person
  skillsMaskOfPerson
dp represents bitmask for people
dp
  initialize with max value of people bitmask, 2 ** (n - 1)
  Base case
    no skill required, empty team is smallest
Find skill that ith person doesn't have
  skills_mask & ~skills_mask_of_person[i]
    e.g. 011 & ~(010) = 011 & 101 = 001
"""

from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)

        skill_to_index = {skill: i for i, skill in enumerate(req_skills)}

        # print(skill_to_index)

        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= (1 << skill_to_index[skill])

        # for i in range(n):
        #     print(f"Person: {i}, skill mask: {bin(skills_mask_of_person[i])}, skills: {people[i]}")

        # Bottom-up DP
        # DP size is (1 << m) because we want m masks for m skills and additional one space for base case of no skill, thus not 2 ** (m - 1)
        # Initialize with max num people of 2 ** (n - 1)
        dp = [(1 << n) - 1] * (1 << m)

        # Base case: No skill, empty team
        dp[0] = 0

        # Recurrence relation
        # 1 << m because it's exclusive, and the final mask we want is (1 << m) - 1
        for skills_mask in range(1, 1 << m):
            for i in range(n):
                # Find skill that ith person doesn't have
                smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]

                if smaller_skills_mask != skills_mask:

                    # people_mask is the new team if wee add current person
                    # new team is union of set of team without current person's skill with current person
                    people_mask = dp[smaller_skills_mask] | (1 << i)

                    # int.bit_count() returns the number of ones in binary representation
                    # If new team (people_mask) has less number of people than current team (dp[skills_mask]),
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask

        # for i in range(len(dp)):
        #     print(f"i: {i}, dp[i]: {dp[i]}, bin(dp[i]): {bin(dp[i])}")

        # Answer mask is the mask with all the skills, which is 2 ** (m - 1)
        ans_mask = dp[(1 << m) - 1]

        # print(f"(1 << m) - 1: {(1 << m) - 1}, ans_mask: {ans_mask}, bin(ans_mask): {bin(ans_mask)}")

        ans = []
        for i in range(n):

            # ans_mask is bitmask for minimum people
            # ans_mask >> i extracts which person
            # e.g. ans_mask: 101 means 0th and 2nd person are needed
            # 101 >> 0 = 101, 101 & is 1
            # 101 >> 1 = 10, 10 & 1 -> 0 & 1 is not 1
            # 101 >> 2 = 1, 1 & 1 is 1
            if (ans_mask >> i) & 1:
                ans.append(i)

        return ans