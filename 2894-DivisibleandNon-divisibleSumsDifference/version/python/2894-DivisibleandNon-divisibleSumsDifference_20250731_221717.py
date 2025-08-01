# Last updated: 7/31/2025, 10:17:17 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sumn = int((n*(n+1))/2)
        summ = 0
        print(sumn)
        if m == 1:
            return - sumn
        for i in range(n+1):
            if abs(i%m) == 0:
                summ = summ + i
        print(summ)
        return int(sumn - 2*summ)