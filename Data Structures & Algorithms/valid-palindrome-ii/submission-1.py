class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def is_pal_range(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                return is_pal_range(left + 1, right) or is_pal_range(left, right - 1)

            left += 1
            right -= 1
            
        return True
        