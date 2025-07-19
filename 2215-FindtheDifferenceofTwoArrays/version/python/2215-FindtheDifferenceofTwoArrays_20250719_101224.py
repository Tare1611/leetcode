# Last updated: 7/19/2025, 10:12:24 AM
# Brute Force Approach is to convert the input list in set to have distinct elements and then check for difference in both set.
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)

        print("n1 == ", n1)
        print("n2 == ", n2)
        n = len(n1)
        m = len(n2)

        res1 = []
        res2 = []
        result = []

        for i in n1:
            if i not in n2:
                res1.append(i)
        
        for j in n2:
            if j not in n1:
                res2.append(j)
        
        result.append(res1)
        result.append(res2)

        return result


        