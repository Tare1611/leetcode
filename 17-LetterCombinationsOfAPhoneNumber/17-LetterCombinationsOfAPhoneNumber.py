# Last updated: 7/29/2025, 11:02:47 AM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Approach - Backtracking to solve using recursion
        # TC - O(n4^n) SC - (4^n)
        res = []

        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backTrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in digitToChar[digits[i]]:
                backTrack(i + 1, currStr + c)
        
        if digits:
            backTrack(0, "")

        return res