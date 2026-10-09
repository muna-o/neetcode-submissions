class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""

        shorter_length = min(len(word1), len(word2))

        print(shorter_length)

        for i in range(shorter_length):
            merged_string += word1[i]
            merged_string += word2[i]

        print(merged_string)

        if len(word1) != len(word2):
            longer_string = word1 if len(word1) > len(word2) else word2
            merged_string += longer_string[shorter_length:len(longer_string)]

        return merged_string
        