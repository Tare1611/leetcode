# Last updated: 8/2/2025, 11:33:24 PM
# Sub Optimal solution
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Approach - Generate an array of the fraction values for the input array
        # - return the pair of indices that generate the kth smallest value
        # 

        result = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                result.append([arr[i],arr[j], arr[i]/arr[j]])
        
        minHeap = []
        for i in range(len(result)):
           heapq.heappush(minHeap, [result[i][2], result[i][0], result[i][1]])
        
        res = 0
        while k > 0:
            a,b,c = heapq.heappop(minHeap)
            k -= 1

        return [b,c]     