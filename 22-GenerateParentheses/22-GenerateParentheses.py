# Last updated: 7/29/2025, 11:02:46 AM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Approach - Only add open parenthesis if open < n
        #  - Only add a closing parenthesis if closed < open
        #  - valid if and only if open == closed == n
        #  - Here open and closed denote to the number of parenthesis we have added to the stack
        #  - We will use back tracking to trace the results
        # TC - O(4^n/sqrt(n))
        # SC - O(n)

        stack = []
        result = []

        def backTrack(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return result
            
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backTrack(openN, closeN + 1)
                stack.pop()

        backTrack(0, 0)

        return result
