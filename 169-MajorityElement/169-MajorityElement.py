# Last updated: 7/28/2025, 11:02:37 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach use the Moore Voting Algorithm
        # TC - O(n) SC - O(1)
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            elif num != candidate:
                count -= 1
        
        # print(candidate)
        return candidate