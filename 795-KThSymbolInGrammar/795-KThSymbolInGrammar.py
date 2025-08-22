# Last updated: 8/22/2025, 4:40:31 PM
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Approach - Use binary search to go through the list and find the 
        # TC - O(log n)
        # SC - O(1)
        curr = 0
        left, right = 1, 2**(n-1)

        for _ in range(n-1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                curr = 0 if curr else 1
        return curr