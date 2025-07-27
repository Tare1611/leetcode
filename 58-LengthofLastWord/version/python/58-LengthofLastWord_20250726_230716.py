# Last updated: 7/26/2025, 11:07:16 PM
# Split the string with spaces and then return the len of last element of split str list
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])