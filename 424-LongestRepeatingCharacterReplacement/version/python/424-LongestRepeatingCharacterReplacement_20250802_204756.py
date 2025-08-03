# Last updated: 8/2/2025, 8:47:56 PM
class Solution:
    def isValid(self, s: str) -> bool:
        # Brute Force Approach - Use a loop and replace the parenthesis.
        # TC - O(n^2), SC - O(1)
        # while '()' in s or '[]' in s or '{}' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('[]', '')
        #     s = s.replace('{}', '')
        # return s == ''
        # Optimal Approach - Use stack to store all the brackets and then pop for each bracket coming up.
        # TC - O(n) SC - O(n)
        stack = []
        brackets = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in brackets:
                if stack and stack[-1] == brackets[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False