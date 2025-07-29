# Last updated: 7/28/2025, 11:02:02 PM
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Approach - Implement a Sliding window and keep updating the outgoing and incoming values and calculate the avg
        # TC - O(n)
        # SC - O(1)

        result = 0
        currSum = sum(arr[:k-1])

        for left in range(len(arr) - k + 1):
            currSum += arr[left + k - 1]
            if  (currSum/k) >= threshold:
                result += 1
            currSum -= arr[left]
        return result
