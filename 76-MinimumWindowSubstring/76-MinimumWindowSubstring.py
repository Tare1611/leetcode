# Last updated: 7/28/2025, 11:02:48 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Approach - Create a map for the substring, keep increasing the window size from 0 to n to check for the substr
        # - Keep a track of the number of letters of the substr that appear
        # TC - O(n)
        # SC - O(n)

        if t == "":
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)

        result = [-1, -1]
        resultLen = float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update result and result length   
                if (r - l + 1) < resultLen:
                    result = [l,r]
                    resultLen = (r - l + 1)
                # pop from the left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l +=1
        
        l, r = result

        return s[l:r+1] if resultLen != float("inf") else ""