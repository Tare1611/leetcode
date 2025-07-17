# Last updated: 7/17/2025, 12:45:11 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Approach is to iterate the flowerbed list and check for the constraints like right and left empty or edge case.
        # TC - O(m) SC - O(1) - m is len of flowerbed
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 0:
                emptyL = (i == 0) or (flowerbed[i-1] == 0)
                emptyR = (i == m-1) or (flowerbed[i+1] == 0)
                if emptyR and emptyL:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0