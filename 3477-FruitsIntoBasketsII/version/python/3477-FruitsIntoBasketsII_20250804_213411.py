# Last updated: 8/4/2025, 9:34:11 PM
# TC - O(n^2) Solution
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # Approach - Loop through the fruits and baskets array and find the first greater than or equal basket
        # - To store the fruit correctly, we could use deque to pop the elements from the left and then return the len

        count = len(fruits)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    count -= 1
                    baskets[j] = 0
                    break
        
        return count