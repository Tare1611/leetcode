# Last updated: 7/19/2025, 3:55:22 PM
class Solution:
    def removeStars(self, s: str) -> str:
        # Brute force approach use stack to store values and pop when *. 
        # TC - O(n^2) SC - O(n)
        # string_stack = []

        # for ch in s:
        #     if ch == '*':
        #         string_stack.pop()
        #     else:
        #         string_stack.append(ch)
        # res_string = ""
        # for i in range(len(string_stack)):
        #     res_string = res_string + string_stack[i]
        # return res_string

        # Optimal Approach - Use inplace join instead of sting concatenation
        # TC - O(n) SC - O(n)

        stack = []
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        
        return ''.join(stack)