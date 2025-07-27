# Last updated: 7/26/2025, 11:10:38 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        prev = 0
        for char in s:
            if char == " " and length != 0:
                prev = length
                length = 0
            elif char != " ":
                length += 1

        return length if length else prev
        
    def lengthOfLastWordEasy(self, s: str) -> int:
        return len(s.split()[-1])