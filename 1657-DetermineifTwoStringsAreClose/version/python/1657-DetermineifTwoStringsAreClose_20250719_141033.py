# Last updated: 7/19/2025, 2:10:33 PM
# Approach is to use stack and append till ']' and then pop until '['.
class Solution:
    def decodeString(self, s: str) -> str:
        # Approach - Have a stack to append all values in str, then when you encounter ']' pop untill '[' and then check for digits and pop them.
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