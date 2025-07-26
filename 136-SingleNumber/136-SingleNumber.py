# Last updated: 7/26/2025, 2:32:45 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach - XOR all the values and at the end you will have just one remaining value
        # TC - O(n) SC - O(1)
        res = 0

        for num in nums:
            res = num ^ res
        return res