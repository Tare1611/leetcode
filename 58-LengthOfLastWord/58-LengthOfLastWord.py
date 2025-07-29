# Last updated: 7/29/2025, 11:02:38 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Approach Split the string and return the len of last element of the list
        return len(s.split()[-1])
