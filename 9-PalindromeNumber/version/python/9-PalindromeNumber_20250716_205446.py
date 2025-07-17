# Last updated: 7/16/2025, 8:54:46 PM
# This is a brute force solution to the problem, where in you just convert the number to string and then check if the reverse is same or not.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Bruteforce approach - convert the number to string and use the string palindrome code
        # TC - O(n), SC - O(n)
        y = str(x)

        return str(x) == y[::-1]


        # if x < 0:
        #     return False
        # og = x
        # y = 0
        # while x!= 0:
        #     digit = x%10
        #     y = y * 10 + digit
        #     x = x//10
        
        # return og == y