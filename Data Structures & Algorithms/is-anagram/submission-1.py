class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for character in s:
            count[ord(character) - ord('a')] += 1
        
        for character in t:
            count[ord(character) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False
            
        return True
