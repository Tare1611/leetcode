# Last updated: 8/24/2025, 12:07:41 PM
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Approach - Sum of odd numbers -> n^2
        # - Sum of even numbers -> n(n+1)
        # - GCD of odd + even = (n^2, n(n+1)) -> n(n, (n+1)) = GCD is n

        return n