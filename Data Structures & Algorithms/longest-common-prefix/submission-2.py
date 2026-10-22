class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        starter = strs[0]

        for i in range(len(starter)):
            for string in strs:
                if i == len(string) or string[i] != starter[i]:
                    return starter[:i]

           
        return starter

        