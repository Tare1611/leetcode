# Last updated: 2/10/2026, 9:19:10 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        
4        # Bruteforce
5        n = nums1 + nums2
6        n.sort()
7        lenn = len(n)
8        if (len(n)%2) != 0:
9            med = int(lenn//2)
10            return float(n[med])
11        else:
12            med1 = int(lenn//2)
13            med2 = int((lenn//2)-1)
14            med = float((n[med1] + n[med2])/2)
15            return med