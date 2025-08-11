# Last updated: 8/10/2025, 7:53:25 PM
class Solution:
    def reverse(self, x: int) -> int:
        # Approach - 
        negBounds = -(2**31)
        posBounds = (2**31) - 1

        print(negBounds)
        print(posBounds)
        if x <= negBounds or x >= posBounds or x == 0:
            return 0
        
        sign = int(x / abs(x))
        revx = 0
        x = abs(x)
        while x:
            add = x % 10
            revx = revx*10 + add
            x = x // 10
        # print(sign)
        if (sign * revx) <= negBounds or (sign * revx) >= posBounds:
            return 0
        return sign*revx