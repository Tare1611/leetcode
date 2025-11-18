# Last updated: 11/17/2025, 9:13:12 PM
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Keep a count on spaces between 1's. if there is a set where the no. of space is smaller than the k.
        spaces = k

        for i in range(len(nums)):
            if nums[i] == 1:
                if spaces < k:
                    return False
                spaces = 0
            else:
                spaces += 1
        return True