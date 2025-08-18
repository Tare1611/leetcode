# Last updated: 8/18/2025, 11:40:45 AM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: 
            return False
        
        s = sqrt(n)
        if s != int(s):
            return False

        s = int(s)
        if (s & (s-1)) == 0:
            return True
        return False