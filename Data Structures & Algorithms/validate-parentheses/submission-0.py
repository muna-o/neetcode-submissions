class Solution:
    def isValid(self, s: str) -> bool:
        matching_strings = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char in matching_strings:
                if not stack:
                    return False
                if stack.pop() != matching_strings[char]:
                    return False
            else:
                stack.append(char)

        return not stack
