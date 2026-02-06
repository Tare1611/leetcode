# Last updated: 2/5/2026, 9:08:07 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        # Approach - Have a 2 pointer setup, where we start with the 1 index
4        # We travel forward considering 0th index is unique and checking with prev
5        # Second pointer is to update the array and keep a track on last
6        # Unique value
7        # TC - O(n)
8        # SC - O(1)
9
10        j = 1
11        
12        for i in range(1, len(nums)):
13            if nums[i] != nums[i-1]:
14                nums[j] = nums[i]
15                j += 1
16        return j