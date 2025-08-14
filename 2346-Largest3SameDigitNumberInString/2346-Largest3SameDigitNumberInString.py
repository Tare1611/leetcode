# Last updated: 8/14/2025, 12:08:58 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        result = "0"
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                result = max((num[i:i+3]), (result))
        return "" if result == "0" else result  