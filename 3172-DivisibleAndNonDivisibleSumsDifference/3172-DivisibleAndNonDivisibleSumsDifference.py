# Last updated: 8/1/2025, 2:11:43 AM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Brute Force Approach - Use the arithmetic progression approach to solve this.
        # TC - O(n) SC - O(1)
        # sumn = int((n*(n+1))/2)
        # summ = 0
        # print(sumn)
        # if m == 1:
        #     return - sumn
        # for i in range(n+1):
        #     if abs(i%m) == 0:
        #         summ = summ + i
        # print(summ)
        # return int(sumn - 2*summ)

        # Supposed Optimal Approach - Use just a for loop
        result = 0
        for i in range(n+1):
            if i%m != 0:
                result = result + i
            else:
                result = result - i
        return result