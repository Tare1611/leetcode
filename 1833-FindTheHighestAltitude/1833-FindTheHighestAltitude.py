# Last updated: 7/19/2025, 12:45:09 AM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Brute Force Approach - Similar to prefix sum but not same. Uses SC - O(n)
        # TC - O(n) SC - O(n) 
        # n = len(gain)
        # alti = [0] * (n + 1)
        # for i in range(n):
        #     if i==0:
        #         alti[i] = gain[i]
        #     if i>0:
        #         alti[i] = alti[i-1] + gain[i]
        # print(gain)
        # print(alti)
        # return max(alti)

        # Optimal Approach - Trying to reduce the SC
        # TC - O(n) SC - O(1)
        alti = 0
        max_alti = 0

        for g in gain:
            alti += g
            max_alti = max(max_alti, alti)
        return max_alti