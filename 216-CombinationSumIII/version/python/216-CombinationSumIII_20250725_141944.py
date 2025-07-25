# Last updated: 7/25/2025, 2:19:44 PM
class Solution:
    def numTilings(self, n: int) -> int:
        # Recursive Approach with two function one for full cover and partial
        # TC - O(n) SC - O(n)

        MOD = 10**9 + 7

        pCache = {}
        nCache = {}

        def partial(n):
            if n == 2:
                return 1
            if n in pCache:
                return pCache[n]
            
            pCache[n] = partial(n-1) + full(n-2)
            return pCache[n]

        def full(n):
            if n <= 2:
                return n
            if n in nCache:
                return nCache[n]
            
            nCache[n] = full(n-1) + full(n-2) + 2 * partial(n-1)
            return nCache[n]

        return full(n) % MOD