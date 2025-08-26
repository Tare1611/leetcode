# Last updated: 8/26/2025, 10:48:43 AM
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Approach - For valid triangle, we need 3 numbers where i <= j < k | i + j > k
        # - First sort the nums
        # - Use loop to take 1 element and then search for the remainging 2 elements 
        # TC - O(n^2)
        # SC - O(1)

        nums.sort()

        result = 0
        for a in range(len(nums)-1, 1, -1):
            b, c = 0, a-1
            while b < c:
                if nums[b] + nums[c] > nums[a]:
                    # Valid Triangle found
                    result += c - b
                    c -= 1
                else:
                    # No valid triangle found, update b
                    b += 1
        return result