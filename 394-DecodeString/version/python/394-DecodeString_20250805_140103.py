# Last updated: 8/5/2025, 2:01:03 PM
# Use stack to store the decoded string
class Solution:
    def decodeString(self, s: str) -> str:
        # Approach - Use stack to store all the characters and symbols 
        # - When you encounter the first closing bracket pop the elements till numeric value
        # - Generate the substring accordingly add it to the stack start checking the stack again.
        # TC - O(n + m)
        # SC - O(n + m)

        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() #removing the "["

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        
        return "".join(stack)