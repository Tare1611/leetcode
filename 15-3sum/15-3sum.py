# Last updated: 7/16/2025, 8:15:14 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force Approach - Use 3 nested for loop and check the condition
        # TC - O(n^3)
        # SC - O(n)
        # n = len(nums)
        # result = set()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        #     return[list(triplet) for triplet in result]
        # Optimal Approach - use sorting and 2 pointer
        # TC - O(n^2), SC - O(n)
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else: 
                    right -= 1
        return result
        