# Last updated: 7/24/2025, 6:32:53 PM
# Binary Search approach with api call.
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        print(n)
        reply = 0
        l = 0
        r = n
        mid = 0
        while l <= r:
            mid = (l+r)//2  
            reply = guess(mid)

            if reply == 0:
                return mid
            elif reply == -1:
                r = mid -1
            else:
                l = mid+1
        