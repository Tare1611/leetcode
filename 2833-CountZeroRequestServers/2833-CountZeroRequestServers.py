# Last updated: 8/5/2025, 6:28:43 PM
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Approach - Sort the logs according to time frame
        # - Also sort the query according to the time but maintain their order for the result array
        # - We have to return the number of servers available for a given query in list format
        # - For calculation subtract x from query to check for the time interval [q[i]-x, q[i]]
        # - Use sliding window to store the result of the current set  of values and just update the outgoing and incoming 


        servers = {i: 0 for i in range(1, n+1)}
        logs.sort(key = lambda x:x[1])
        queries = sorted([[query, i] for i, query in enumerate(queries)])

        L = len(logs)
        Q = len(queries)
        res = [0] * Q

        no_requests = n
        left, right = 0, 0
        for query, i in queries:
            while right < L and logs[right][1] <= query:
                server = logs[right][0]
                if servers[server] == 0:
                    no_requests -= 1
                servers[server] += 1
                right += 1
            while left < L and logs[left][1] < query - x:
                server = logs[left][0]
                if servers[server] == 1:
                    no_requests += 1
                servers[server] -= 1
                left += 1
            res[i] = no_requests
        return res