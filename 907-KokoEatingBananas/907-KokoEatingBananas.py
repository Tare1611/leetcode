# Last updated: 7/26/2025, 2:32:18 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Approach - Since we know that the length of piles <= h, we can take a range from 1 to max of piles and check for the range where the k <= h for that instance. We need to find the minimum. We can use binary search for the range selection
        # TC- O(nlogm) where m is max pilesize and n is len of piles SC - O(1)
        import math
        m = max(piles)
        left = 1 
        right = m
        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res           