class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        for i in range(len(sentence)):

            if sentence[i] == " ":
                if sentence[i - 1] != sentence[i + 1]:
                    return False

        return sentence[0] == sentence[-1]

    def isCircularSentence1(self, sentence: str) -> bool:
        words = sentence.split(" ")

        for i in range(len(words)):

            if i == 0:
                if words[i][0] != words[-1][-1]:
                    return False
            else:
                if words[i][0] != words[i - 1][-1]:
                    return False

        return True