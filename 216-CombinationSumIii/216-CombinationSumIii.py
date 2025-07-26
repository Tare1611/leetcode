# Last updated: 7/26/2025, 2:32:38 PM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Approach - Use stack to check for the combination, use recursion to find len of "k" and matches "n"
        # TC - O(k * C(9, k)) SC - O(k * C(9, k))
        # output = []

        # def dfs(build, num, sum_s):
        #     # base case - if build len is k and sum_s is n
        #     if len(build) == k:
        #         if sum_s == n:
        #             output.append(build)
        #         return
            
        #     # recursion loop
        #     for i in range(num, 9+1):
        #         if sum_s + i > n:
        #             break
        #         dfs(build + [i], i + 1, sum_s + i)
        # dfs([], 1, 0)

        # return output


        # Second Approach is to use iter tools to find all the combinations and then check for the sum if it matches to n
        # TC - O(k * C(9, k)) SC - O(k * C(9, k))

        nums = [i for i in range(1, 9+1)]

        combinations = itertools.combinations(nums, k)

        return [c for c in combinations if sum(c) == n]