# Last updated: 8/24/2025, 8:13:01 PM
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # Approach - Start from a point in between 0 index and last index
        # - Work to check the ascending values from both left and right
        # - Update the result by multiplying the left small and right large values
        # - For descending values subtract left_small from m and right large from length and m and -1
        
        result = 0

        for m in range(1, len(rating) - 1):
            left_small = 0
            right_large = 0
            
            # Finding the ascending triplet
            for i in range(m):
                if rating[i] < rating[m]:
                    left_small += 1
            
            for i in range(m+1, len(rating)):
                if rating[i] > rating[m]:
                    right_large += 1
            
            result += left_small * right_large

            # Calculating the descending triplet
            left_large = m - left_small
            right_small = len(rating) - m - 1 - right_large

            result += left_large * right_small
        return result