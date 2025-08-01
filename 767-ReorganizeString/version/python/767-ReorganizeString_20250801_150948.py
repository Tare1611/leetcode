# Last updated: 8/1/2025, 3:09:48 PM
# Use maxHeap to store the frequency of each character.
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Approach - Use Max heap to store the count of each character and then generate the output
        # TC - O(n log k)
        # SC - O(n)

        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        result = ""

        while maxHeap or prev:
            # most freq, except prev
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return result
