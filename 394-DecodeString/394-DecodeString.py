# Last updated: 7/19/2025, 3:55:35 PM
class Solution:
    def decodeString(self, s: str) -> str:
        # Approach - Have a stack to append all values in str, then when you encounter ']' pop until '[' and then check for digits and pop them.
        # TC - O(n) SC - O(n)
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        
        return ''.join(stack)