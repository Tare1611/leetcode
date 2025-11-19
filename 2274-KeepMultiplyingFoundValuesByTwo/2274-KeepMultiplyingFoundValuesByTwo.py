# Last updated: 11/19/2025, 12:09:51 AM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        orig = original

        while orig in nums:
            orig = orig*2
        return orig