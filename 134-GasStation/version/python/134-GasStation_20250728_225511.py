# Last updated: 7/28/2025, 10:55:11 PM
# Running two while loops to check for the correct set of parenthesis
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Approach - Traverse through the str and check for each parenthesis, do it twice once from left next from right, return max_len
        # TC - O(n) - running the while loop twice
        # SC - O(1)
        
        open_P = 0
        close_P = 0
        max_len = 0
        
        i = 0

        while i < len(s):
            if s[i] == "(":
                open_P += 1
            else: 
                close_P += 1

            if open_P == close_P:
                max_len = max(max_len, open_P + close_P)
            elif close_P > open_P:
                open_P = close_P = 0
            i += 1

        open_P = close_P = 0

        i = len(s) - 1 
        while i >= 0:
            if s[i] == "(":
                open_P += 1
            else: 
                close_P += 1

            if open_P == close_P:
                max_len = max(max_len, open_P + close_P)
            elif close_P < open_P:
                open_P = close_P = 0
            i -= 1

        return max_len