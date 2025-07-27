# Last updated: 7/26/2025, 8:43:45 PM
# Two pointer, one pointer updates the array with non value numbers
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Approach - take a pointer to update the first element of the array and move forward
        # TC - O(n) SC - O(1)
        # prevlen = len(nums)
        left = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
        # print(nums)
        return left
        # return left - 1