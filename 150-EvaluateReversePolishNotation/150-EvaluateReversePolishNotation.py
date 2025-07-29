# Last updated: 7/28/2025, 11:02:40 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Approach - Use a stack to store the digits and pop them to perform the calculation, append back the result
        # TC - O(n) since using a single for loop
        # SC - O(n) since using a stack to store the numbers
        
        res = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                stack.append(tokens[i])
            elif tokens[i] == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a + b
                stack.append(res)
            elif tokens[i] == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a - b
                stack.append(res)
            elif tokens[i] == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a * b
                stack.append(res)
            elif tokens[i] == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a / b
                stack.append(res)
            else:
                stack.append(tokens[i])

        return int(stack[0])