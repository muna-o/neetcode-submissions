class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        length = len(strs[0])

        for i in range(length):
            for element in strs:
                if i >= len(element) or strs[0][i] != element[i]:
                    return element[0:i]

        return strs[0]
        