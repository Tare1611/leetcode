# Last updated: 7/19/2025, 3:03:52 PM
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Approach - Maintain 2 queues for senate and check the index and then pop
        # TC - O(n) SC - O(n)
        from collections import deque
        n = len(senate)
        r = deque()
        d = deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                r.append(i)
            else:
                d. append(i)
        
        while r and d:
            radiant = r.popleft()
            dire = d.popleft()
            if radiant < dire:
                r.append(radiant + n)
            else:
                d.append(dire + n)

        return "Radiant" if r else "Dire"