# Last updated: 2/5/2026, 6:51:36 PM
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Approach - Have a result set to avoid duplicates. Check through the range intervals to find out common values,
        # - Sort the intervals according to the end and possibly merge the intervals with common end make sure to have atleast
        # - 2 common elements while merging. Perform this for the whole array of intervals. Then start identifying the common
        # - values. Push them to set
        # - Return the length of set

        # 1. Sort: End time Ascending, then Start time Descending
        intervals.sort(key=lambda x: (x[1], -x[0]))       
        # print(intervals)
        
        # 2. Initialize trackers
        # p1 is the second largest selected number
        # p2 is the largest selected number
        # Start them at -1 so they don't intersect with valid range [0, 10^8]
        p1, p2 = -1, -1
        ans = 0

        # 3. Iterate through sorted intervals
        for s, e in intervals:

            # Case 1: No Overlap (s > p2)
            # Neither p1 nor p2 falls in this interval.
            # We must add 2 numbers. We pick the largest available: e-1 and e.
            if s > p2:
                ans += 2
                p1 = e - 1
                p2 = e

            # Case 2: Partial Overlap (s > p1)
            # p2 is inside [s, e], but p1 is below s.
            # We have 1 valid number (p2), so we need 1 more.
            # We pick the largest available: e.
            elif s > p1:
                ans += 1
                p1 = p2
                p2 = e

            # Case 3: Full Overlap (s <= p1)
            # Both p1 and p2 are inside [s, e].
            # We already have 2 numbers covering this interval.
            else:
                continue
        return ans
                
