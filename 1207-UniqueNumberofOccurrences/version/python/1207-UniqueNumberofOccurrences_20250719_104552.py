# Last updated: 7/19/2025, 10:45:52 AM
# This is approach uses dictionary to map key value pairs and then I am using set to find difference.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for item in arr:
            freq[item] = freq.get(item, 0) + 1

        print(freq)
        res1 =set(freq.values())
        print(res1)

        if len(res1) == len(freq):
            return True
        
        return False
