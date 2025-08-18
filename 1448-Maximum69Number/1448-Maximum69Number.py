# Last updated: 8/18/2025, 11:40:07 AM
class Solution:
    def maximum69Number (self, num: int) -> int:
        
        s = str(num)

        if not "6" in s:
            return num
        
        index = s.index("6")
        return int(s[:index] + "9" + s[index+1:])