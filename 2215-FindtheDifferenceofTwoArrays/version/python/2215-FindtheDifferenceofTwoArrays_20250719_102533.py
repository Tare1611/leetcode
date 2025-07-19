# Last updated: 7/19/2025, 10:25:33 AM
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Brute Force Approach - Convert the list to sets to remove duplicates and then run for loop to check for intersection
        # TC - O(n + m) SC - O(n + m)

        # n1 = set(nums1)
        # n2 = set(nums2)

        # # print("n1 == ", n1)
        # # print("n2 == ", n2)

        # res1 = []
        # res2 = []
        # for i in n1:
        #     if i not in n2:
        #         res1.append(i)
        
        # for j in n2:
        #     if j not in n1:
        #         res2.append(j)

        # return [res1,res2]

        # Cleaner Approach with less lines of code same convert ot set and then do set1-set2 and vice versa.
        n1 = set(nums1)
        n2 = set(nums2)

        return [list(n1-n2), list(n2-n1)]


        