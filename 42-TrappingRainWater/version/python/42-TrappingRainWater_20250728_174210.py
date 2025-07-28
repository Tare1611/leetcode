# Last updated: 7/28/2025, 5:42:10 PM
# Loop approach with deque to store values, not the best
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Approach - Use a deque and work with a loop to reach "k"
        # TC - O(n*k)
        # SC - O(n)
        q = deque()
        
        for i in range( 1, n + 1):
            q.append(i)
        
        while len(q) > 1:
            for i in range(k - 1):
                num = q.popleft()
                q.append(num)
            q.popleft()
        
        return q[0]

        # Optimal Approach - Do it in one pass to reduce running time
        # TC - O(n)
        # SC - O(1)

        