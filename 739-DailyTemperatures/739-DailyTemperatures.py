# Last updated: 7/26/2025, 2:32:22 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force Approach - Use two for loops to traverse through the array twice
        # TC - O(n^2)  SC - O(n)

        # n = len(temperatures)
        # result = [0]*n
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[i] < temperatures[j]:
        #             result[i] = j-i
        #             break

        # return result

        # Optimal Approach - Use monotonic decreasing stack (decreasing order), trade space for better time
        # TC - O(n) SC - O(n)

        n = len(temperatures)
        result = [0]*n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        return result
                