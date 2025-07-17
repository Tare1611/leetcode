# Last updated: 7/16/2025, 8:14:54 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force approach - Use for loop and then check further conditions
        # TC - O(n), SC - O(n)
        # num_index = {}
        # for i, num in enumerate(numbers):
        #     complement = target - num
        #     if complement in num_index:
        #         return [num_index[complement], i+1]
        #     num_index[num] = i+1
        # return [] 
        # Trying to achieve SC - O(1), use two pointer and work on array itself
        # TC - O(n), SC - O(1)
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return []
