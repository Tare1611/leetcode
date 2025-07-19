# Last updated: 7/19/2025, 1:06:16 PM
# Brute Force Approach - Use a stack to add character values from string before * and then pop if * encountered.
class Solution:
    def removeStars(self, s: str) -> str:
        string_stack = []

        for ch in s:
            if ch == '*':
                string_stack.pop()
            else:
                string_stack.append(ch)
        res_string = ""
        for i in range(len(string_stack)):
            res_string = res_string + string_stack[i]
        return res_string