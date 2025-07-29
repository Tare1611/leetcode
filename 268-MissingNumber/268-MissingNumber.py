# Last updated: 7/29/2025, 4:34:48 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        actual = ((n)*(n+1))//2
        current = sum(nums)
        return actual - current