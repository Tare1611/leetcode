# Last updated: 7/19/2025, 11:33:56 AM
# Cleaner Approach using Counter Library
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Approach - Use a dictionary to store key-value pair and then use the len function to check.
        # TC - O(n) SC - O(n)
        # freq = {}
        # for item in arr:
        #     freq[item] = freq.get(item, 0) + 1
        # print(freq)
        # res1 =set(freq.values())
        # print(res1)
        # if len(res1) == len(freq):
        #     return True
        # return False

        # Cleaner Approach - Use counter to create the freq map and then again len to check
        from collections import Counter
        freq = Counter(arr)

        return len(set(freq.values())) == len(freq)