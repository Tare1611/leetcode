# Last updated: 8/6/2025, 1:13:20 PM
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Approach - Perform calculation for the first child, update n and then check for the remaining 2
        # - If the condition still satisfies the n and limit then update the number of combinations.
        # TC - O(limit)
        # SC - O(1)

        # combinations = 0

        # for i in range(min(n, limit) + 1):
        #     after_first = n - i
        #     if after_first > 2 * limit:
        #         continue
            
        #     second_at_least = max(after_first - limit, 0)
        #     second_at_most = min(after_first, limit)
        #     combinations += second_at_most - second_at_least + 1

        # return combinations

        # Approach - Using combinatorics to reduce TC and SC. 
        # TC - O(1)
        # SC - O(1)

        def count(n):
            return comb(n + 2, 2) if n >= 0 else 0
        
        total = count(n)
        one_exceed = 3 * count(n - (limit + 1))
        two_exceed = 3 * count(n - 2 * (limit + 1))
        three_exceed = count(n - 3 * (limit + 1))

        return total - one_exceed + two_exceed - three_exceed