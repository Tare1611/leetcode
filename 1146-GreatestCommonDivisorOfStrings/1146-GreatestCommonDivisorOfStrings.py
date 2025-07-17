# Last updated: 7/17/2025, 12:45:10 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Optimal Approach is to first check if both the string when added are same or not. Then use math library to find gcd.
        # TC - O( n + m ) SC - O( n + m )
        if str1 + str2 != str2 + str1:
            return ""
        gcdlen = math.gcd(len(str1), len(str2))
        return str1[:gcdlen]