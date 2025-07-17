# Last updated: 7/16/2025, 8:14:48 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute Force Approach - Use a comparision and sorted method
        # TC - O(nlogn + mlogm) Where n and m are the lengths of two strings
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        # Optimal Approach - use Hash Map with the help of a Dict
        # TC - O(n+m)  Where n and m are the lengths of two strings
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT