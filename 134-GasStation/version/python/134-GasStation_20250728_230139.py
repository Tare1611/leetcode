# Last updated: 7/28/2025, 11:01:39 PM
# Trading space for Speed. Using stack for faster execution.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base index
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

        