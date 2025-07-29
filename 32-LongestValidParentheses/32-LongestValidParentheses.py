# Last updated: 7/29/2025, 11:02:41 AM
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Approach - Traverse through the str and check for each parenthesis, do it twice once from left next from right, return max_len
        # TC - O(n) - running the while loop twice
        # SC - O(1)
        
        # open_P = 0
        # close_P = 0
        # max_len = 0
        
        # i = 0

        # while i < len(s):
        #     if s[i] == "(":
        #         open_P += 1
        #     else: 
        #         close_P += 1

        #     if open_P == close_P:
        #         max_len = max(max_len, open_P + close_P)
        #     elif close_P > open_P:
        #         open_P = close_P = 0
        #     i += 1

        # open_P = close_P = 0

        # i = len(s) - 1 
        # while i >= 0:
        #     if s[i] == "(":
        #         open_P += 1
        #     else: 
        #         close_P += 1

        #     if open_P == close_P:
        #         max_len = max(max_len, open_P + close_P)
        #     elif close_P < open_P:
        #         open_P = close_P = 0
        #     i -= 1

        # return max_len


        # Optimal Approach - Use stack and trace the amount of the parenthesis added to the stack. Will use single loop
        # TC - O(n)
        # SC - O(n) - Trading space for faster execution

        stack = [-1]
        max_len = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len