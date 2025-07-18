# Last updated: 7/18/2025, 2:46:06 PM
# Implementation of sliding window with vowels set.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Brute Force Approach - 2 For Loops giving TLE for large input.
        # TC - O(n^2) SC - O(1)
        # vowels = ('a','e','i','o','u')
        # n = len(s)
        # count = 0
        # max_count = 0
        # for i in range(n - k + 1):
        #     count = 0
        #     for j in range(i, i + k):
        #         if s[j] in vowels:
        #             count += 1
        #     max_count = max(max_count, count)
        # return max_count

        # Optimal Approach - Use Sliding window and update count
        # TC - O(n) SC - O(1)
        vowels = set('aeiou')
        max_count = 0
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = max(max_count, count)

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_count = max(max_count, count)
        return max_count