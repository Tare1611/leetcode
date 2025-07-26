# Last updated: 7/26/2025, 2:32:10 PM
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Approach - Start checking from the non significant bit and flip if required according to the OR and & operator
        # TC - O(n)  SC - O(1)

        flips = 0

        while a>0 or b>0 or c>0:
            aBit = a & 1
            bBit = b & 1
            cBit = c & 1
            if cBit == 1:
                if (aBit|bBit) != 1:
                    flips += 1
            else:
                if aBit == 1:
                    flips += 1
                if bBit == 1:
                    flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips