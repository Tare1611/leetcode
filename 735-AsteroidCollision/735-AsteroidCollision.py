# Last updated: 7/16/2025, 8:14:38 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # for asteroid in asteroids:
        #     stack.append(asteroid)
        # # print(stack)
        # # print("Stack pop one time", stack.pop())
        # # print("Stack pop second time", stack.pop())

        # while len(stack) > 1:
        #     a = stack.pop()
        #     print(a)
        #     b = stack.pop()
        #     print(b)
        #     if a*b < 0:
        #         if abs(a) > abs(b):
        #             stack.append(a)
        #         elif abs(a) < abs(b):
        #             stack.append(b)
        #         # elif abs(a) == abs(b):
        #             # continue 
        #     else:
        #         stack.append(b)
        #         stack.append(a)
        #         break
        # print(stack)
        # return stack

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                # checking if stack is there and a is negative or not 
                if stack[-1] < -a: #checking if 
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack