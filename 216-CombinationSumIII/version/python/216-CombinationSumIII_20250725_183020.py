# Last updated: 7/25/2025, 6:30:20 PM
# Using sort and then looping through the list to find the intervals to delete
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Approach - sort the intervals and then loop through the list to check and remove
        # TC - O(nlogn)  SC - O(n)

        intervals.sort()
        n = len(intervals)
        result = 0 
        
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # If start is greater than or equals to prevEnd then update end and continue
                prevEnd = end
            else:
                # Deleting the interval (tracking how many we delete)
                result += 1
                prevEnd = min(prevEnd, end)
        return result