# Last updated: 8/9/2025, 6:06:25 PM
class Solution:
    def processStr(self, s: str) -> str:
        
        # Approach use an array to store the incoming characters and while displaying the output use str and join
        # TC - O(n)
        # SC - O(n)
        
        n = len(s)

        result = ""
        
        for ch in s:
            if ch == "*":
                result = result[:-1]
            elif ch == "#":
                result = result + result
            elif ch == "%":
                result = result[::-1]
            elif ch.islower():
                result += ch
        # print(result)
        return result
