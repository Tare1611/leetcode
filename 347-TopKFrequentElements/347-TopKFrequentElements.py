# Last updated: 7/16/2025, 8:14:45 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force Approach - use sorted and lambda function with freq map
        # TC - O(nlogn)
        freq_map = Counter(nums)
        sort_items = sorted(freq_map.items(), key=lambda x:x[1], reverse=True)
        return [item[0] for item in sort_items[:k]]
        #  Optimal Approach - Use Heapq
        # TC - O(nlogk)
        # freq_map = Counter(nums)