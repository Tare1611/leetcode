# Last updated: 7/29/2025, 2:47:32 PM
# Using the addition till n formula to get the correct answer
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        actual = ((n)*(n+1))//2
        current = sum(nums)
        return actual - current