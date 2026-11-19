class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0

        length_1 = len(word1)
        length_2 = len(word2)

        merged = []

        while i < length_1 or j < length_2:
            if i < length_1:
                merged.append(word1[i])
                i += 1

            if j < length_2:
                merged.append(word2[j])
                j += 1

        return "".join(merged)
        