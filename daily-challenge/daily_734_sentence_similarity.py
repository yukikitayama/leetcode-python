from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        similarity_set = set()
        for a, b in similarPairs:
            similarity_set.add((a, b))

        # print(similarity_set)

        for a, b in zip(sentence1, sentence2):

            if a == b:
                continue

            if (a, b) not in similarity_set and (b, a) not in similarity_set:

                # print(f'(a, b): {(a, b)}')

                return False

        return True


if __name__ == "__main__":
    sentence1 = ["great", "acting", "skills"]
    sentence2 = ["fine", "drama", "talent"]
    similarPairs = [
        ["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
    # True

    sentence1 = ["great"]
    sentence2 = ["great"]
    similarPairs = []
    # True
    print(Solution().areSentencesSimilar(sentence1, sentence2, similarPairs))


