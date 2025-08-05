# Last updated: 8/5/2025, 12:06:17 PM
# Use a hash map of prefix sum and the frequency of the sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #  Approach - Use a hash Map to store all the prefix sum and their count.
        # - Update the result variable with the value from the hash Map and return result
        # TC - O(n)
        # SC - O(n)

        result = 0
        currSum = 0
        prefixSum = {0 : 1}

        for num in nums:
            currSum += num
            diff = currSum - k

            result += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        
        return result