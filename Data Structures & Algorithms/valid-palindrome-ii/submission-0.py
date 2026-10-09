class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validPalindromeRange(word: str, left: int, right: int) -> bool:
            while left < right:
                if word[left] != word[right]:
                    return False

                left += 1
                right -= 1
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return validPalindromeRange(s, left, right - 1) or validPalindromeRange(s, left + 1, right)
            left += 1
            right -= 1


        return True
        