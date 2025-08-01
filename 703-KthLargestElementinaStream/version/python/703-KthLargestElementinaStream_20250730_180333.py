# Last updated: 7/30/2025, 6:03:33 PM
# Use of MinHeap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Brute Force or intuitive approach is to sort the array and then return required value.
        # TC - O(nlogn) - sort function TC, SC - O(1)
        # nums.sort()
        # n = len(nums)
        # return nums[n-k]
        
        # Optimal Approach - Use heapq to store the values of nums
        # TC - O(n logk) SC - O(k)
        import heapq
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]