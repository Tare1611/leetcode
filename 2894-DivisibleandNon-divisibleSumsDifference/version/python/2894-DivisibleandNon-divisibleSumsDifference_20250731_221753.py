# Last updated: 7/31/2025, 10:17:53 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num_1=0
        num_2=0     
        for i in range(1,n+1):
            if i%m != 0:
                num_1+=i
            elif i%m==0:
                num_2+=i
        return num_1-num_2      