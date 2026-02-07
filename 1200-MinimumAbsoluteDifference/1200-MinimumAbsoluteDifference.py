# Last updated: 2/6/2026, 9:58:37 PM
1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        # Approach - Sort the array and then keep track of the difference and update min diff
4        # TC - O(nlogn)
5        # SC - O(n)
6        arr.sort()
7        # print(arr)
8        result = []
9        min_diff = float('inf')
10
11        for i in range(1, len(arr)):
12            diff = arr[i] - arr[i-1]
13            if diff < min_diff:
14                res = [[arr[i-1], arr[i]]]
15                min_diff = diff
16            elif diff == min_diff:
17                res.append([arr[i-1], arr[i]])
18        return res
19