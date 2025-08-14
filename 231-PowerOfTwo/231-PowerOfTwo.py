# Last updated: 8/14/2025, 12:09:50 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        elif (n & (n-1)) == 0:
            return True
        else:
            return False