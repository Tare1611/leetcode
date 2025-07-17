# Last updated: 7/16/2025, 8:56:52 PM
# This is the updated solution without using the string conversion.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Bruteforce approach - convert the number to string and use the string palindrome code
        # TC - O(n), SC - O(n)
        # y = str(x)

        # return str(x) == y[::-1]

        # Optimal Approach - Without converting the number to string reverse using while loop
        # TC - O(log10 X) SC - O(1)
        if x < 0:
            return False
        og = x
        y = 0
        while x!= 0:
            digit = x%10
            y = y * 10 + digit
            x = x//10
        
        return og == y