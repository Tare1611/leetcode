# Last updated: 7/16/2025, 8:15:00 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force Approach - Keep track of the streak and use nested loop
        # TC - O(n^2)
        # longest_streak = 0
        # for num in nums:
        #     current_num = num
        #     current_streak = 1
        #     while (current_num + 1) in nums:
        #         current_num += 1
        #         current_streak += 1
        #     longest_streak = max(longest_streak, current_streak)
        # return longest_streak
        # Optimal Approach - use Hashset to reduce iterations
        # TC - O()
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak