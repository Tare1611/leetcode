# Last updated: 8/1/2025, 7:27:25 PM
# Implement Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach - pass the nums list to a counter and then create a minHeap of the result.
        # - Pop the elements from heap till count of k
        # TC - O(klogn)
        # SC - O(n)
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in  count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
