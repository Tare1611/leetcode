# Last updated: 8/1/2025, 6:01:12 PM
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Approach - Find the count of k in the given array. 
        # TC - O(50*n)
        # SC - O(1)

        startFreq = nums.count(k)
        maxDupes = 0

        for i in range(1,51):
            if i == k:
                continue
            currFreq = 0
            currMax = 0

            for num in nums:
                if num == i:
                    currFreq += 1
                elif num == k:
                    currFreq -= 1
                currFreq = max(currFreq, 0)
                currMax = max(currMax, currFreq)
            maxDupes = max(maxDupes, currMax)
        return maxDupes + startFreq