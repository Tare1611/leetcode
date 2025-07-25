# Last updated: 7/25/2025, 4:51:49 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach - XOR all the values and at the end you will have just one remaining value
        # TC - O(n) SC - O(1)
        res = 0

        for num in nums:
            res = num ^ res
        return res