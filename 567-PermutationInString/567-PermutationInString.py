# Last updated: 7/16/2025, 8:14:41 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force Approach - 2 for loop, sort s1 and check with sorted substring of s2
        # TC - O(n^3 logn)
        # SC - O(n)
        # s1 = sorted(s1)
        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         sub = s2[i: j+1]
        #         sub = sorted(sub)
        #         if sub == s1:
        #             return True
        # return False
        # Optimal Approach - Create a sliding window for s2 and check against s1
        # TC - O(n)
        # Sc - O(1)
        if len(s1) > len(s2):
            return False
        
        s1count, s2count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)
        l = 0
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 ==s2count[index]:
                matches -= 1
            l += 1
        return matches == 26

