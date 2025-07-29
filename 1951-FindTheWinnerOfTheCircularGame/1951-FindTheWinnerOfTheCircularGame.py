# Last updated: 7/28/2025, 11:01:56 PM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Approach - Use a deque and work with a loop to reach "k"
        # TC - O(n*k)
        # SC - O(n)
        # q = deque()
        
        # for i in range( 1, n + 1):
        #     q.append(i)
        
        # while len(q) > 1:
        #     for i in range(k - 1):
        #         num = q.popleft()
        #         q.append(num)
        #     q.popleft()
        
        # return q[0]

        # Optimal Approach - Use recursion to reduce the running time and space used.
        # TC - O(n)
        # SC - O(n) Due to recursion stack

        def helper(n, k):
            if n == 1:
                return 0
            return(helper(n-1, k) + k) % n
        return helper(n, k) + 1

