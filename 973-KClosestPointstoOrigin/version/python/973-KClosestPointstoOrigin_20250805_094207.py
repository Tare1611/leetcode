# Last updated: 8/5/2025, 9:42:07 AM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (sort_by, point)
        result = []
        for point in points:
            x_coord, y_coord = point[0], point[1]

            sort_by = abs(x_coord)**2 + abs(y_coord)**2
            result.append((sort_by, point))

        final_result = []
        pairs = sorted(result, key=lambda x: x[0])[:k]
        for pair in pairs:
            final_result.append(pair[1])
        
        return final_result