class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Pointers initially point to first character and last character
        left = 0
        right = len(s) - 1

        while left < right:
            # Swaps the values held in the places referred to by the pointers
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            # Moves to closer values in aray
            left += 1
            right -= 1

        