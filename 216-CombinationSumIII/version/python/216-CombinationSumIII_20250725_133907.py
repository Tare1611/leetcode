# Last updated: 7/25/2025, 1:39:07 PM
# DP and reverse looping to select the smallest value and jump count
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Approach - Use dp and reverse tracking the cost array to find the correct values. 
        # TC - O(n) - SC - O(n)
        
        cost.append(0)
        n = len(cost)
        for i in range( n - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        print(cost)
        return min(cost[0], cost[1])