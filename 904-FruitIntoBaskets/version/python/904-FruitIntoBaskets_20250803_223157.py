# Last updated: 8/3/2025, 10:31:57 PM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Approach - Use a set to store the visited tree type, and increment the count of the fruit.
        # - Return the max sum of two baskets, use a sliding window to check for the largest contiguous subarray.
        # - TC - O(n)
        # - SC - O(1)

        start = 0 
        maxLen = 0
        fruit_count = defaultdict(int)

        for end in range(len(fruits)):
            fruit_count[fruits[end]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1
            maxLen = max(maxLen, end - start + 1)
        return maxLen