# Last updated: 8/5/2025, 4:26:32 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Approach - Loop through the array, and check if the element is divisible or not and update the result accordingly
        # TC - O(n)
        # SC - O(1)
        result = 0
        for i in range(n+1):
            if i%m != 0:
                result = result + i
            else:
                result = result - i
        return result