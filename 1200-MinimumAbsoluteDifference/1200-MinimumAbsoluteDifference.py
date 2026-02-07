# Last updated: 2/6/2026, 9:57:55 PM
1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        # Approach - Sort the array 
4        arr.sort()
5        # print(arr)
6        result = []
7        min_diff = float('inf')
8
9        for i in range(1, len(arr)):
10            diff = arr[i] - arr[i-1]
11            if diff < min_diff:
12                res = [[arr[i-1], arr[i]]]
13                min_diff = diff
14            elif diff == min_diff:
15                res.append([arr[i-1], arr[i]])
16        return res
17