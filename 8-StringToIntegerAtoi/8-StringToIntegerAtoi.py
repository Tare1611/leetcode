# Last updated: 7/16/2025, 8:15:17 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        # Brute force approach - use a while loop to check through the string for digits and break if there is anything apart from digit
        # TC - O(n) SC - O(n) since using the "num_str"
        # s = s.lstrip()
        # if not s:
        #     return 0
        
        # i = 0
        # sign = 1
        # num_str = ""

        # if s[0] == "-":
        #     sign = -1
        #     i += 1
        # elif s[0] == "+":
        #     sign = 1
        #     i += 1
        
        # while i < len(s):
        #     if s[i].isdigit():
        #         num_str += s[i]
        #     else:
        #         break
        #     i += 1
        
        # if not num_str:
        #     return 0
        
        # num = int(num_str)*sign

        # int_min = -2**31
        # int_max = 2**31-1

        # if num < int_min:
        #     return int_min
        # elif num > int_max:
        #     return int_max
        # return num

        # Optimal Ap(proach - Store the number directly removing the need for num_str
        s = s.lstrip()
        if not s:
            return 0
        
        i = 0
        num = 0
        sign = 1

        if s[0] == "-":
            sign = -1
            i += 1
        elif s[0] == "+":
            sign = 1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1
        
        num *= sign
        
        int_min = -2**31
        int_max = 2**31-1

        if num < int_min:
            return int_min
        elif num > int_max:
            return int_max
        return num