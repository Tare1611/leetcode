# Last updated: 7/16/2025, 8:14:40 PM
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base_k(n: int, k: int) -> str:
            res = []
            while n > 0:
                res.append(str(n % k))
                n //= k
            return ''.join(reversed(res))
        def generate_palindromes():
            length = 1
            while True:
                # Odd length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[-2::-1])  # Odd length
                # Even length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])    # Even length
                length += 1

        count = 0
        total = 0
        for num in generate_palindromes():
            if is_palindrome(to_base_k(num, k)):
                total += num
                count += 1
                if count == n:
                    break
        return total