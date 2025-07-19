# Last updated: 7/19/2025, 1:33:58 PM
'''
Use stack and pop the top if incoming is bigger, pop both if same, pop incoming if smaller, else append a.
TC - O(n)
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Approach - have a stack and check for the sign first and the compare abs value
        # TC - O(n) SC - O(n)

        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack