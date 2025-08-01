# Last updated: 7/31/2025, 10:25:03 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(1, n+1):
            if i % m != 0:
                res += i
            else:
                res -= i
        return res        