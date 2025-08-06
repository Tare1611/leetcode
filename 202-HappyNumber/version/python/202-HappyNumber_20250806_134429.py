# Last updated: 8/6/2025, 1:44:29 PM
# Loop to with infinity check using set
class Solution:
    def isHappy(self, n: int) -> bool:
        # Approach - Break the n and get the sum of squares of its constituent numbers
        # - Store all the values in set to stop the endless loop
        # - Also if n == 1 return True
        # - Will use a helper function to generate the sum of squares 

        def sumOfSquare(n: int) -> int:
            output = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                output += digit
                n = n // 10
            return output

        visited = set()
        while n not in visited:
            visited.add(n)

            if n == 1:
                return True
            
            n = sumOfSquare(n)
        
        return False
