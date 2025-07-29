# Last updated: 7/29/2025, 1:27:03 PM
# Updated comments for the optimal solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Two for loop check approach.
        # TC - O(n^2) Sc - O(1)
        # n = len(s)

        # for i in range(n):
        #     flag = True
        #     for j in range(n):
        #         if i!=j and s[i]==s[j]:
        #             flag = False
        #             break
            
        #     if flag:
        #         return i
        # return -1

        # Approach - Use a counter to count and store the frequency for each character in the string.
        # TC - O(n)
        # SC - O(n)
        from collections import Counter
        count = Counter(s)

        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
