# Last updated: 7/16/2025, 8:15:18 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the arrays and sort them, then apply the median finding algorithm where if the length is even take 2 values and average, if odd take the middle value of sorted array.
        n = nums1 + nums2
        n.sort()
        # print(n)
        lenN = len(n)
        
        median = 0

        if lenN%2 == 0:
            a = int(lenN//2)
            # print(a)
            b = int((lenN//2) - 1)
            # print(b)
            median = (n[a] + n[b])/2
            # print(median)
        else:
            c = int(lenN//2)
            # print(c)
            median = n[c]
            # print(median)
        return median