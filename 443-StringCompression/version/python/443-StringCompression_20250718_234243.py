# Last updated: 7/18/2025, 11:42:43 PM
# My Approach use a single for loop. TC - O(n)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alti = [0] * (n + 1)
        for i in range(n):
            if i==0:
                alti[i] = gain[i]
            if i>0:
                alti[i] = alti[i-1] + gain[i]
        print(gain)
        print(alti)
        return max(alti)