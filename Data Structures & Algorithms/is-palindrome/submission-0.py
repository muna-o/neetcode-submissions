class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Thoughts:

        Approach 1: Iterate through the string, and create a new string that removes any characters that are not alphanumeric. Then, use two pointers to determine if it's a palindrome.


        Approach 2 (not creating new string):
        use two pointers apprach (like you would use if it's all alphanumeric).
        If you come across a character that is not alphanumeric, while loop until it is alphanumeric (but make sure left pointer never goes)
        '''
        # Approach 1

        alpha_char = []

        for char in s:
            if char.isalnum():
                alpha_char.append(char)

        left, right = 0, len(alpha_char) - 1

        while left < right:
            if alpha_char[left].lower() != alpha_char[right].lower():
                return False
            left += 1 
            right -= 1
        return True
        