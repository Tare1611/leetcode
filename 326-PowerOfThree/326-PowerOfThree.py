# Last updated: 8/14/2025, 12:09:45 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        

        if n <= 0: 
            return False
        
        while n % 3 == 0:
            n = n //3
        return n == 1