# Last updated: 7/28/2025, 3:30:15 PM
# Floyd's Tortoise Hare
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Approach - Use Floyd's Tortoise Hare Algo
        # TC - O(n) 
        # SC - O(1)

        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow