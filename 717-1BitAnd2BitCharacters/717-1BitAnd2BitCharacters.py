# Last updated: 11/19/2025, 1:00:45 AM
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else: 
                i += 2
        return i == len(bits) - 1
